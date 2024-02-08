from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def slash():
    return "Миссия Колонизация Марса"


@app.route("/index", methods=["GET"])
def index():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    app.run("127.0.0.1", port=8080, debug=True)
