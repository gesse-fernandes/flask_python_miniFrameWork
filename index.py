from flask import Flask,render_template,request,session,make_response,redirect
import pymysql
app = Flask(__name__)
app.secret_key = '123'
db = pymysql.connect(host="localhost",user='root',password='',database='youtube')
@app.route("/",methods=["GET",'POST'])
def hello_flask():
    cursor = db.cursor()
    sql = "SELECT * FROM clientes"
    cursor.execute(sql)
    results = cursor.fetchall()
    '''
    if request.method == "GET":
        
        if  request.cookies.get("usuario"):
            resp = make_response('My Web Site')

            
        else:
            resp = make_response("meu web site sem cookie")
            resp.set_cookie('usuario','gesse')
        
        return resp 
        #return render_template("index.html",content = ['banana','perl,','ok'])
    elif request.method == "POST":
        return request.form['name']
    '''
    return render_template('index.html',content = results )

@app.route("/deletar",methods=['GET','POST'])
def deletar():
    
    cursor = db.cursor()
    sql = "DELETE from clientes where id = %s"
    cursor.execute(sql,(request.args.get("id"),))
    db.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)