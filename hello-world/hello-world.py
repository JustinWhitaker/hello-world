import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Method used: %s' % request.method


@app.route('/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are using GET'


@app.route('/profile/<username>')
def profile(username):
    return '<h2>Hi, %s!</h2>' % username


if __name__ == "__main__":
    app.run()
