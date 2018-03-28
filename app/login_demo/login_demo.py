#coding:utf8

from flask import Blueprint , render_template

#  创建蓝图 第一个参数为蓝图的名字
login = Blueprint('login',__name__)

@login.route('/login/<username>')
def login_demo(username):
    # return 'login'
    return render_template("hello.html",name=username)
