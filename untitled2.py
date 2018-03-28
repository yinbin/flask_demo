# from flask import Flask
# from flask import render_template
#
#
# app = Flask(__name__)
# app.debug = True
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!12'
#
# @app.route('/test/<username>')
# def hello_world2(username):
#     return 'Hello World %s' % username
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
#
# @app.route('/name/<username>')
# def showname(username):
#     return render_template("hello.html", name=username)
# # if __name__ == '__main__':
# #     app.run()
