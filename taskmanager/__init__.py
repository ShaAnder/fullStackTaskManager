# WE are creating all our imports / app in the init file as
# we want this to be a package.

# imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#check for our env file if it exists import (we will have our envs on heroku)
if os.path.exists("env.py"):
    import env


# define our app parameters, secret key, url
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# create our app
db = SQLAlchemy(app)

# we want to import this after app and db or we get circular import errors
# so this MUST be imported AFTER those two are defined
from taskmanager import routes