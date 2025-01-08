# Part of the MVC architecture (models views controllers) models contains our 
# models handle our data logic as well as our database interactions

from taskmanager import db

class Category(db.Model):
    # schema for the category model
    id = db.Column(db.Integer, primary_key=True)
    # string = #chars allows, unique = can't be duped, nullable = can't be empty
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # here we are linking tasks table to the category table, relationship is a hidden
    # Column that won't be displayed unlike Column. 
    # Task = links to task table
    # backref = links it back to this table, 
    # cascade all, delete = select and delete all records associated with the cascade
    # lazy true = this will set lazy loading to default select, loading stuff as it's accessed
    # for the first time, you can set this depending on how to load it if at all
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    #schema for the table model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    # text = allows for longer strings, similar to text area
    task_description = db.Column(db.Text, nullable=False)
    # bool for true false on the tast, default = default setting
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    # integer = number, foreignkey = links to category, points to id primarykey
    # ondelete="CASCADE" => we want to be able to delete all tasks associated with
    # one category, but not the reverse, CASCADE achieves this by removing all associated
    # tasks when the singular category (foreign linked to primary) key is deleted
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        # we can either return self or a formatted string. A formatted string is more pythonic
        # and also allows us to create a neater return
        return "#{task_id} // Task: {task_name} | This task {task_urgency} urgent".format(
            task_id = self.id, 
            task_name = self.task_name, 
            task_urgency ="is" if self.is_urgent else "is not"
        )
