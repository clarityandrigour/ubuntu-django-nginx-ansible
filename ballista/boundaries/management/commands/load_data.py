# Django setings

from django.core.management.base import BaseCommand
from django.conf import settings
from django.apps import apps

from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import LayerMapping

import boundaries.models

# Python

from zipfile import ZipFile
import pathlib
import string

class Command(BaseCommand):
    help = "Loads data from shapefiles"

    def add_arguments(self, parser):
        parser.add_argument('-m', '--models', nargs='*',
                            help='Lower case, punctuation stripped, space separated list of models to process.')

    def handle(self, *args, **kwargs):

        shapefile_dir = pathlib.Path(settings.BASE_DIR) / 'data'
        models = kwargs['models']

        TARGET_APP = 'boundaries'

        canonical_models = apps.all_models[TARGET_APP]
        cleaned_models = [mdl.lower().strip('_').translate(str.maketrans('', '', string.punctuation)) for mdl in models]

        print(canonical_models)

        kwargs = {
                    'cleaned_models': cleaned_models,
                    'canonical_models': canonical_models,
                    'TARGET_APP': TARGET_APP,
                    'shapefile_dir': shapefile_dir
                  }

        result = execute_loading(**kwargs)

        if result:
            print("Success")
        else:
            print("Failure")


def get_models_to_run(cleaned_models, canonical_models):
    good_models = []
    bad_models = []

    for model in cleaned_models:
        if model.lower().strip(' ') in canonical_models:
            good_models.append(model)
        else:
            bad_models.append(model)

    if len(bad_models) > 0:
        print('You specified the following non-existent models: {bad_models}'.format(**{'bad_models': bad_models}))

    if len(good_models) > 0:
        print("You specified the following valid models: {good_models}".format(**{'good_models': good_models}))
        return good_models
    else:
        return False


def execute_loading(**kwargs):
    """Master function"""

    print("Master function")

    cleaned_models = kwargs['cleaned_models']
    canonical_models=kwargs['canonical_models']
    target_app = kwargs['TARGET_APP']
    shapefile_dir = kwargs['shapefile_dir']

    agenda_models = get_models_to_run(cleaned_models=cleaned_models, canonical_models=canonical_models)

    for mdl in agenda_models:

        short_name = mdl
        zip_name = short_name + '.zip'
        shapefile_name = short_name + '.shp'
        model_class = canonical_models[mdl]
        mapping_name = short_name + '_mapping'

        mapping = getattr(boundaries.models, mapping_name)

        # shapefile manipulation
        shapefile_zip = shapefile_dir / zip_name
        shapefile_target = shapefile_dir

        with ZipFile(shapefile_zip, 'r') as zipObj:
            # Extract all the contents of zip file in current directory
            zipObj.extractall(path=shapefile_target)

        shapefile_shp = str(shapefile_target / short_name / shapefile_name)

        spatial_data_source = DataSource(shapefile_shp)

        # clear all objects

        while model_class.objects.count() > 0:
            model_class.objects.all().delete()

        try:
            lm = LayerMapping(model_class, spatial_data_source, mapping, transform=True)
            lm.save(verbose=False, strict=True)

        except Exception as ex:

            print("There was an error at the command level: {0}".format(ex))


