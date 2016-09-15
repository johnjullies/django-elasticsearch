# django-elasticsearch
I want to learn how to implement a search form in Django from Elastic search
and a bit of googling lead me to [this tutorial](https://qbox.io/blog/how-to-elasticsearch-python-django-part1).

# Prerequisite
`Python` (I'm using `2.7.10`)  
`virtualenv`  
`Elasticsearch` (I'm using the 2.3.5 docker image)

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
Run Elasticsearch server on port `9200:9200`. If you're using the
docker image like me, run

    docker run -p 9200:9200 -d elasticsearch:2.3.5
Populate the database and elasticsearch server with dummy data 

    python manage.py dummy-data 10000
    python manage.py push-to-index
Create a superuser then you can run the dev server.

    python manage.py createsuperuser
    python manage.py runserver
