from flask import Blueprint

admin_aa = Blueprint('admin',__name__)


@admin_aa.route('/admin')
def reg():
    return 'admin'