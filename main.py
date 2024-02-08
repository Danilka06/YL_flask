from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def slash():
    return "Миссия Колонизация Марса"


@app.route("/index", methods=["GET"])
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion", methods=["GET"])
def promotion():
    return render_template("index.html")


if __name__ == '__main__':
    app.run("127.0.0.1", port=8080, debug=True)
