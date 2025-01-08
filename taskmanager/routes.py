from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    return render_template("add-items.html")

@app.route("/tasks")
def tasks():
    return render_template("tasks.html")

#when user adds a category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    #if method is post (user submitted information)
    if request.method == "POST":
        #create a new category object with the category name being the request
        category = Category(category_name=request.form.get("category_name"))
        #add and commit it to the session
        db.session.add(category)
        db.session.commit()
        # categories = db.session.query(Category)
        # for c in categories:
        #     db.session.delete(c)
        #     db.session.commit()
        return redirect(url_for("home"))
    #we create a cursor object (array) that we can pass to the template
    view_categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("add-category.html", categories=view_categories)

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("add_category"))
    return render_template("edit-category.html", category=category)
    
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    view_categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("add-category.html", categories=view_categories)

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add-task.html", categories=categories)

@app.route("/contact")
def contact():
    return render_template("contact.html")