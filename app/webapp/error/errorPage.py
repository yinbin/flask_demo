# -*- coding: utf-8 -*-
from app.config.application import app

"""
@Author:yinbinhome@163.com
@Description:全局404定义
@Time:2020/02/21 10:47 AM
"""


@app.errorhandler(404)
def error_404(arg):
    '''自定义错误页面，根据状态码定制'''
    return "404错误啦"
