# -*- coding: utf-8 -*-

from app.config.application import app
from flask import render_template, request, redirect, session

"""
@Author:yinbinhome@163.com
@Description:request拦截器，可以在request之前和之后进行拦截，做一些响应处理
@Time:2020/02/20 5:01 PM
"""


@app.before_request
def login():
    print('before_request')
    # if request.path == '/admin':
    #     username = request.args.get('username')
    #     if username != 'admin':
    #         print ('没有权限')
    #         return redirect('/')
    #     else:
    #         print 'success'


@app.after_request
def getUser(environ):
    print('after_request')
    return environ
