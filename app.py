from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.db"

db = SQLAlchemy(app)

from routes import *


if __name__ == "__main__":
    app.run(debug=True)
    
    from models import *
    with app.app_context():
        db.create_all()