from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('http://www.baidu.com')


@app.route('/user/<username>')
def user(username):
    return "<h1>Hello, %s</h1>" % username


if __name__ == '__main__':
    app.run(debug=True)
