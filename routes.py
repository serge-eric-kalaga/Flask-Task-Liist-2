from app import app
from flask import render_template
import forms

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/about", methods=['POST', 'GET'])
def about():
    form = forms.AddTaskForm()
    title = None
    
    if form.validate_on_submit():
        title = form.title.data
    return render_template('about.html', form=form, title=title)