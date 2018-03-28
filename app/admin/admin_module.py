from flask import Blueprint

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/aa')
def index():
    return '<h1>Hello, this is admin blueprint11</h1>'