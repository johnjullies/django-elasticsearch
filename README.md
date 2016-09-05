# django-elasticsearch
I want to learn how to implement a search form in Django from Elastic search
and a bit of googling lead me to [this tutorial](https://qbox.io/blog/how-to-elasticsearch-python-django-part1).

# Prerequisite
`Python` (I'm using `2.7.10`)  
`virtualenv`

# Setup
Create and go into the virtual environment

    virtualenv .env
    . .env/bin/activate
Install Django and other dependencies listed in requirements.txt

    pip install -r requirements.txt

Get inside the project directory and build the database

    cd project/
    python manage.py makemigrations core
    python manage.py migrate

Create a superuser then you can run the dev server.

    python manage.py createsuperuser
    python manage.py runserver
