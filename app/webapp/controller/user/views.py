# coding: utf-8

import json

from flask import Blueprint
from flask import jsonify

from app.db.database import db
from app.webapp.model.model import User

user = Blueprint('user',__name__)

user_data = [
    {
        'id': 1,
        'name': '张三',
        'age': 23
    },
    {
        'id': 2,
        'name': '李四',
        'age': 24
    }
]


@user.route('/<int:id>', methods=['GET', ])
def get(id):
    for user in user_data:
        if user['id'] == id:
            return jsonify(status='success', user=user)


@user.route('/users', methods=['GET', ])
def users():
    data = {
        'status': 'success',
        'users': user_data
    }

    admins = User.query.filter_by(username='yinbin')
    print (admins[0].show())
    sql="select * from user where username='admin'"
    users=db.session.execute(sql)
    for u in users:
        print(u.username)
        print(u.email)
        print u
    return json.dumps(data, ensure_ascii=False, indent=1)