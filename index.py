from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "<h2>Hello Flask top oh rapaz e não é que mudou mesmo</h2>"


if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)