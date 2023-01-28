from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/",methods=["GET",'POST'])
def hello_flask():
    if request.method == "GET":

        return render_template("index.html",content = ['banana','perl,','ok'])
    elif request.method == "POST":
        return request.form['name']


if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)