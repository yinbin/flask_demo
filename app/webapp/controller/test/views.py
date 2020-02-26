# coding: utf-8

import json

from flask import Blueprint
from flask import jsonify

from app.db.database import *
from app.webapp.model.model import User

test = Blueprint('test',__name__)

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


@test.route('/<int:id>', methods=['GET', ])
def get(id):
    for user in user_data:
        if user['id'] == id:
            return jsonify(status='success', user=user)


@test.route('/test', methods=['GET', ])
def users():
    data = {
        'status': 'success',
        'users': user_data
    }

    admins = User.query.filter_by(username='yinbin')
    print (admins[0].show())
    # print (len(admins))
    sql="select * from user limit 100"
    users=db.session.execute(sql).fetchall()
    print(users)
    # for u in users:
    #     print u._asdict()
    return json.dumps(users, cls=AlchemyJsonEncoder)