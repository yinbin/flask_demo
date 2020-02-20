# coding: utf-8
from sqlalchemy import Column, String
from app.db.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<name %r>' % self.username

    def show(self):
        print self.username+'|'+self.email

class TArea(db.Model):
    __tablename__ = 't_area'

    id = Column(db.Integer, primary_key=True)
    name = Column(String(30))
    level = Column(db.Integer)
    pid = Column(db.Integer)
    flag = Column(db.Integer)

    def __repr__(self):
        return '[%r' % self.name+']'

    def show(self):
        print self.name + '|' + str(self.level)
