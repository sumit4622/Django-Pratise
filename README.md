# Django Practice Setup

This document outlines the steps to set up a Django project using a virtual environment.

## Install Virtualenv
- `pip3 install virtualenv`

## Creating virtual folder
- `python -m venv <folderName>`

## Activating virtual environment
- `<folderName>\Scripts\activate`  *(Windows)*  
  or  
- `source <folderName>/bin/activate` *(macOS/Linux)*

## Install Django
- `pip install django`

## Create a Django Project
- `django-admin startproject <projectname>`

## Run the Django Project
- `python manage.py runserver`
