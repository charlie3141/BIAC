from flask_sqlalchemy import SQLAlchemy
from config import db 

class Users(db.Model) : 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(80), nullable = False)
    pwd = db.Column(db.String(80), nullable = False)
    def to_json(self):
        return {
            "id" : self.id,
            "email" : self.email,
            "pwd" : self.pwd
                }
        