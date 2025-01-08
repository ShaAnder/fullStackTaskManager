## ABOUT



A small Task manager application utilizing a flask base with sql for the backend and a materialize framework for the front end. 

View deployed app [here](https://full-stack-task-manager-33d103367644.herokuapp.com) (currently down for bug fixing)

The purpose of this app was to demonstrate knowledge of full stack technologies as part of my Diploma in full stack software development.

As this was originally a follow along project, I opted to take the same approach I usually do, try and learn / implement things differently
and often before the current implementation is being covered. Only following the lessons if i had exhausted all other options.

Technologies used:

HTML
CSS
JS
Materialize
Flask
SQLAlchemy

As this app uses older packages to run, as some are not supported with newer flask, the following pip command is required
to get the app to run in a local setting

```
pip install -r requirements.txt
```

Creation steps (mainly for my own note):


## CREATING THE BACKEND

(1) FIRST: I created the file base with the following structure:

taskmanager
    |
    |templates
        |
        |base.html
    __init__.py
    models.py
    routes.py
.gitignore
env.py
README.md
requirements.txt
run.py

The base contains our html template for all pages
The models contains our database class models
Routes are for our page routing
env.py handles our environment variables including connection settings
our run.py handles running our app

We added the requirements.txt as an alternative to the lesson plans solution as
that was installing a newer conflicting version of flask

(2) SECOND: I set the db and migrated the models over to the database with python, this was fairly straight forward and required us to just login, create a database and migrate

Set and login to psql
```
set_pg
psql
```
Create and change to our DB
```
CREATE DATABASE taskmanager;
\c taskmanager
\q
```
Use python to migrate
```
(in cli) 
python3
from taskmanager import db
db.create_all()
```

Edit if we edit the models later we need to remigrate the models later
Also to check if the tables populated correctly we use:

```
psql -d taskmanager
\dt
```

## CREATING THE FRONTEND
