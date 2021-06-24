from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/Filip')
def hello_filip():
    return 'Hello Filip!'


if __name__ == '__main__':
    app.run()
