from flask import Flask, render_template,request,redirect,session,url_for
import sqlite3
app= Flask(__name__)

app.secret_key = "123"
conn= sqlite3.connect("signup.db",check_same_thread=False)

@app.route("/", methods = ['GET' , 'POST'])
def home():
    msg= None
    if(request.method == "POST"):
       if(request.form.get("name") !="" and request.form.get("username") !="" and request.form.get("password") !=""):
           username = request.form.get("username")
           name = request.form.get("name")
           password = request.form.get("password")
           c = conn.cursor()
           params=(username,name,password)
           c.execute("INSERT INTO db1 VALUES (?,?,?)",params)
           conn.commit()
       else :
           msg = 'Please add all the fields'
           
           
    return render_template("index.html", msg=msg)

@app.route("/login" ,methods = ['GET' , 'POST'])
def login():
    r = ''
    msg = ''
    msg2=''
    if(request.method == "POST"):
         name = request.form.get("nm")
         if( name =="" ):
             msg = "please enter username"
         else :
             params=(name,)
             c = conn.cursor()
             c.execute("SELECT * FROM db1 WHERE username = ?",params)
             #c.execute("select * from db1 WHERE username=?".format(name))
             r = c.fetchall()
         if r=='':
             msg='User not found'
         else:
             for i in r:
                 msg=i[0]
                 msg2=i[1]
 
    return render_template('login.html', msg=msg,msg2=msg2)     
    
@app.route("/delete",methods = ['GET' , 'POST'])
def home1():
    r = ''
    msg = ''
    
    if(request.method == "POST"):
         name = request.form.get("nm")
         if( name =="" ):
             msg = "please enter username"
             print(name)
         else :
             c = conn.cursor()
             params=(name,)
             c.execute("SELECT * FROM db1 WHERE username = ?",params)
             r = c.fetchall()
             print('checking user ')
         if r=='':
             msg='User not found'
         else:
             conn= sqlite3.connect("signup.db")
             c = conn.cursor()
             print('deleting data')
             params=(name,)
             c.execute("DELETE FROM db1 WHERE username = ?",params)
             conn.commit()
             msg='User data successfully deleted'
             
    return render_template("delete.html",msg=msg)


@app.route("/update",methods = ['GET' , 'POST'])
def update():
      msg=''
      uname=''
      name=''
      if(request.method == "POST"):
         uname = request.form.get("nm")
         name = request.form.get("name")
         print(uname , name)
         if( uname =="" ):
             msg = "please enter username"
         else:
             c = conn.cursor()
             print('update data')
             params=(name,uname)
             c.execute("UPDATE db1 SET name = ? WHERE username = ?",params)
             conn.commit()
             msg='User data successfully updated' 
          
      return render_template("update.html",msg=msg)
    
if __name__ == '__main__':
    app.run(debug= True)
