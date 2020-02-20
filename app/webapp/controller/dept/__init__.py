# coding:utf-8
from flask import Blueprint

dept = Blueprint('dept', __name__,)

from app.webapp.controller.dept import views