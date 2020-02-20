# coding:utf-8
from flask import Blueprint

user = Blueprint('user', __name__,)

from app.webapp.controller.user import views