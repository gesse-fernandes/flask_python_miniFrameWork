from flask import Flask,render_template,request,session,make_response
import pymysql
app = Flask(__name__)
app.secret_key = '123'
db = pymysql.connect(host="localhost",user='root',password='',database='youtube')
@app.route("/",methods=["GET",'POST'])
def hello_flask():
    if request.method == "GET":
        
        if  request.cookies.get("usuario"):
            resp = make_response('My Web Site')

            
        else:
            resp = make_response("meu web site sem cookie")
            resp.set_cookie('usuario','gesse')
        cursor = db.cursor()
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results[0][1])
        return resp 
        #return render_template("index.html",content = ['banana','perl,','ok'])
    elif request.method == "POST":
        return request.form['name']


if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)