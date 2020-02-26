# coding: utf-8


import json
from flask_sqlalchemy import SQLAlchemy,BaseQuery
from app.config.application import app

# 数据库连接信息
user = 'root'
pwd = '123456'
database = 'test'

# 创建flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + user + ':' + pwd + '@localhost/' + database
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class AlchemyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseQuery):
            # an SQLAlchemy class
            fields = []
            record = {}
            for rec in obj.all():
                for field in [x for x in dir(rec) if
                              not x.startswith('_')
                              and hasattr(rec.__getattribute__(x), '__call__') == False
                              and x != 'metadata']:
                    data = rec.__getattribute__(field)
                    try:
                        # json.dumps(data)  # this will fail on non-encodable values, like other classes
                        record[field] = data
                    except TypeError:
                        record[field] = None
                fields.append(record)
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)