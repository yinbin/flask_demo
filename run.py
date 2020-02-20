#coding:utf8

from app.db.database import app
from app.webapp.router import router

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # print( app.url_map )
    app.run(port=8090)