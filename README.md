# Welcome To The Generic Django Development Environment

This is a GIS project template written by Dheeraj Chand of [Clarity and Rigour](http://www.clarityandrigour.com) (email: first_initial+last_name AT clarity and rigour DOT COM, strip the spaces and do the subs).
This template:

1. Is written in [Python](http://www.python.org),
2. Uses [PostgreSQL](http://www.postgresql.org) as the database, with [PostGIS](http://www.postgis.net) extensions,
3. Uses [GeoDjango](http://www.geodjango.org) as the application framework and
4. Uses [R](http://www.r-project.org) for computations.
5. Uses [Hadoop](http://hadoop.apache.org) and [Hive](https://hive.apache.org)

## The purpose of this project.

This project allows you to have a new Django project from scratch via Ansible + Vagrant. The main components are:

- [Ubuntu 18.04](http://www.ubuntu.com)
- [Python 3.6.7](http://www.python.org)
- [PostgreSQL 10.8](http://www.postgresql.org)
- [PostGIS 2](http://www.postgis.net)
- [GeoServer](http:///www.geoserver.org)
- [nginx](http://www.nginx.org)
- [gunicorn](http://gunicorn-docs.readthedocs.org/en/19.3/)
- [R](http://www.r-project.org)
- [npm](http://www.npmjs.com)

### Sources

Nothing happens in a vacuum. I got a lot of help. Here are some of the references I used that warrant special mention. The general inspiration came from [Wercker](http://blog.wercker.com/2013/11/25/django-16-part3.html) and the set of instructions that I modified slightly came from [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04?comment=47694). Specific problems I found either by googling for Ansible techniques, asking Jonathan for help or by using the following links:


1. [Installing JRE 7 in Vagrant](https://gist.github.com/arturaz/5243940)
2. [Setting the Java Home variable correctly](https://www.digitalocean.com/community/tutorials/how-to-install-java-on-ubuntu-with-apt-get)
3. [Installing Tomcat for GeoServer](https://www.digitalocean.com/community/tutorials/how-to-install-apache-tomcat-7-on-ubuntu-14-04-via-apt-get)
4. [Hadoop](https://www.tutorialspoint.com/hadoop/hadoop_enviornment_setup.htm)
5. [Hive](https://www.tutorialspoint.com/hive/hive_installation.htm)
6. [Getting Django to Work In Ubuntu 18](https://www.cloudbooklet.com/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-in-google-cloud/)

## Repo Contents

1. Vagrantfile + Ansible Playbook for virtual machine config. Ansible inspiration from [this project], and configuration instructions modified from 
2. Code for a generic Django 2.10 project at the top level of the repo, which you can configure to your liking.

## Host Environment

### Install VirtualBox
https://www.virtualbox.org/wiki/Downloads

### Install Vagrant
https://www.vagrantup.com/downloads.html

### Install Ansible
http://docs.ansible.com/intro_installation.html

## Development Environment
Make sure git doesn't change line endings:
```
git config --global core.autocrlf input
```

## Startup
You will need to edit the vars.yaml file. This file contains the project name, user names and passwords. Please set them according to your preferences. ***THIS IS NON-DISCRETIONARY. Tomcat will not run correctly without this.***

Start VM with Vagrant. This will use Ansible to install dependencies and run a script to set up virtual environment and pip requirements.
```
vagrant up --provision
```
Open browser to http://localhost:8080 to check that everything works. It should show the Django start page that tells you to configure URL's.

You will also need to create your own Django superuser for the project. You can do that by:

```
vagrant ssh
python manage.py createsuperuser
```

or by using the manage.py tool in your IDE. [PyCharm](https://www.jetbrains.com/pycharm/) has that built in!

To configure your GeoServer, you will need to go to [http://localhost:8081/geoserver](http://localhost:8081/geoserver) and log in. The default credentials are *admin* , *geoserver*.  From there, you can do whatever you need. 

## Geting Started

1. Create the superuser as above
2. Visit [http://localhost:8080/admin](http://localhost:8080/admin) to ensure that data are loaded.
3. If they are not, `python manage.py load_data` will do so for you. Then do step 2.


## Management
If you make any changes to Vagrantfile, requirements.txt, or default.pp:
```
vagrant reload --provision
```
If you need to shut down or reboot your laptop, or just want to stop the VM:
```
vagrant halt
```
To log onto VM:
```
vagrant ssh
```
To get rid of a VM if you are done or it was corrupted:
```
vagrant destroy
```
If you a change is made to Vagrantfile or requirements.txt, do
```
vagrant reload -–provision
```