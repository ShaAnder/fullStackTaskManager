from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    return render_template("add-items.html")

@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

@app.route("/add_task", methods=["GET", "POST"])
def add_category():
    return render_template("add-category.html")

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    return render_template("add-category.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")