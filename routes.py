from app import app
from flask import render_template
import forms
from models import Task

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/about", methods=['POST', 'GET'])
def about():
    form = forms.AddTaskForm()
    title = None
    tasks = Task.getall()
    
    if form.validate_on_submit():
        title = form.title.data
        task = Task(title=title)
        task.add()
    return render_template('about.html', tasks=tasks, form=form, title=title)