#coding:utf8

from app.db.database import app
from app.webapp.router import router
from flask import render_template,request,redirect
from app.webapp.intercepter import filter_login
from app.webapp.error import errorPage

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # print( app.url_map )
    app.run(port=8090)