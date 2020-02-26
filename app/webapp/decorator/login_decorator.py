# -*- coding: utf-8 -*-

from flask import  request, redirect, session


"""
@Author:yinbinhome@163.com
@Description:
@Time:2020/02/21 10:35 AM
"""


# 定义一个装饰器用于拦截用户登录
# func是使用该修饰符的地方是视图函数
def login_require(func):
    def decorator(*args, **kwargs):
        # 现在是模拟登录，获取用户名，项目开发中获取session
        username = request.args.get('USER_NAME')
        # 判断用户名存在且用户名是什么的时候直接那个视图函数
        if username and username == 'admin':
            return func(*args, **kwargs)
        else:
            # 如果没有就重定向到登录页面
            return redirect("login/yb")

    return decorator
