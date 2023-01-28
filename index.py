from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return render_template("index.html",content = ['banana','perl,','ok'])


if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)