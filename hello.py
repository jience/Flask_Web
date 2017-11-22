from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)


if __name__ == '__main__':
    manager.run()
