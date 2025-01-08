from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    return render_template("add-items.html")

@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        # db.session.add(category)
        # db.session.commit()
        categories = db.session.query(Category)
        for c in categories:
            db.session.delete(c)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add-category.html")

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    return render_template("add-category.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")