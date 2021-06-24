from flask import render_template
from app import app

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/Filip')
def hello_filip():
    return render_template("filip.html")


if __name__ == '__main__':
    app.run()
