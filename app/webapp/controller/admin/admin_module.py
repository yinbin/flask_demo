from flask import Blueprint
from app.webapp.decorator.login_decorator import *

admin_aa = Blueprint('admin',__name__)


@admin_aa.route('/admin')
@login_require
def reg():
    return 'admin'