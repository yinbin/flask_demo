# -*- coding: utf-8 -*-


"""
@Author:yinbinhome@163.com
@Description:路由定义文件，使用蓝图
@Time:2020/02/20 3:24 PM
"""
from app.webapp.controller.login_demo.login_demo import login    # 从分路由倒入路由函数
from app.webapp.controller.admin.admin_module import admin_aa
from app.webapp.controller.register_demo.register_demo import register
from app.webapp.controller.user.views import user
from app.webapp.controller.test.views import test


from app.db.database import app

# 注册蓝图 第一个参数 是蓝图对象
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(admin_aa)
app.register_blueprint(user)
app.register_blueprint(test)


