# -*- coding: utf-8 -*-

from flask import Flask
"""
@Author:yinbinhome@163.com
@Description:
@Time:2020/02/20 4:26 PM
"""

# 创建flask
# 在需要flask的地方需要引用此文件或者此app变量
app = Flask(__name__,template_folder='../../templates')
#使用session 先设置secret_key
app.secret_key='123456'
app.debug = True