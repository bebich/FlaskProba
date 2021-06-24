from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/Filip')
def hello_world():
    return 'Hello Filip!'


if __name__ == '__main__':
    app.run()
