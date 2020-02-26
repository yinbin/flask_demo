# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


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
