from app import db
from datetime import datetime
from werkzeug.exceptions import NotFound

class Task(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return self.title
    
    def __init__(self, title):
        self.title = title
        

    @classmethod
    def get(cls, id) :
        if id=="" or id==None :
            raise NotFound()
        return cls.query.filter_by(id=id).first_or_404('Task not found')
    
    @classmethod
    def delete(cls, id):
        task = cls.get(id)
        task.delete() 
        db.session.commit()
    
    
    @classmethod
    def getall(cls) :
        return cls.query.all()
    
    def add(self):
        db.session.add(self)
        db.session.commit()