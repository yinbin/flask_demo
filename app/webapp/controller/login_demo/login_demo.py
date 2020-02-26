# coding:utf8

from flask import Blueprint, render_template, session

#  创建蓝图 第一个参数为蓝图的名字
login = Blueprint('login', __name__)


@login.route('/login/<username>')
def login_demo(username):
    # return 'login'
    session['USER_NAME']=username
    return render_template("login/hello.html", name=username)
