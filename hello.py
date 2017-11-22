from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Bad Request</h1>", 400


@app.route('/user/<username>')
def user(username):
    return "<h1>Hello, %s</h1>" % username


if __name__ == '__main__':
    app.run(debug=True)
