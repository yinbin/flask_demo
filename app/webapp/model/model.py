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


class StudentUser(db.Model):
    __tablename__ = 'student_user'

    id = db.Column(db.Integer, primary_key=True)
    oid = db.Column(db.String(10), index=True)
    yiyuan_name = db.Column(db.String(100), index=True)
    sheng = db.Column(db.String(30))
    shi = db.Column(db.String(50))
    qu = db.Column(db.String(20))
    ysh_id = db.Column(db.String(20))
    level = db.Column(db.String(50))
    is_save = db.Column(db.Integer, server_default=db.FetchedValue())
    is_push = db.Column(db.Integer, server_default=db.FetchedValue())
    flag1 = db.Column(db.Integer)
    province = db.Column(db.String(20))
    city = db.Column(db.String(20))
    district = db.Column(db.String(20))