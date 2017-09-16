import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Index!"


@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('profile.html',name=name)


if __name__ == "__main__":
    app.run()
