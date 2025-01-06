from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    return render_template("tasks.html")

@app.route("/about")
def contact():
    return render_template("contact.html")

@app.route("/contact")
def about():
    return render_template("about.html")