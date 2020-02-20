# coding: utf-8



from flask_sqlalchemy import SQLAlchemy
from app.config.config import app

# 数据库连接信息
user = 'root'
pwd = '123456'
database = 'test'

# 创建flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + user + ':' + pwd + '@localhost/' + database
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
