from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return "<p>Your browser is %s</p>" % user_agent


@app.route('/user/<username>')
def user(username):
    return "<h1>Hello, %s</h1>" % username


if __name__ == '__main__':
    app.run(debug=True)
