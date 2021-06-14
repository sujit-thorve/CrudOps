from flask import Flask, render_template,request,redirect,session,url_for
import sqlite3
app= Flask(__name__)

app.secret_key = "123"


@app.route("/", methods = ['GET' , 'POST'])
def home():
    msg= None
    if(request.method == "POST"):
       if(request.form.get("name") !="" and request.form.get("username") !="" and request.form.get("password") !=""):
           username = request.form.get("username")
           name = request.form.get("name")
           password = request.form.get("password")
           conn= sqlite3.connect("signup.db")
           c = conn.cursor()
           print(username,name,password)
           c.execute("INSERT INTO db1 VALUES ('"+name+"','"+username+"','"+password+"')")
           
           conn.commit()
           conn.close()
        
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
             conn= sqlite3.connect("signup.db")
             c = conn.cursor()
             c.execute("SELECT * FROM db1 WHERE username = '"+name+"' ")
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
             conn= sqlite3.connect("signup.db")
             c = conn.cursor()
             c.execute("SELECT * FROM db1 WHERE username = '"+name+"' ")
             r = c.fetchall()
             print('checking user ')
         if r=='':
             msg='User not found'
         else:
             conn= sqlite3.connect("signup.db")
             c = conn.cursor()
             print('deleting data')
             c.execute("DELETE FROM db1 WHERE username = '"+name+"' ")
             conn.commit()
             conn.close()
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
             conn= sqlite3.connect("signup.db")
             c = conn.cursor()
             print('update data')
             c.execute("UPDATE db1 SET name = '"+name+"' WHERE username = '"+uname+"' ")
             conn.commit()
             conn.close()
             msg='User data successfully updated' 
          
      return render_template("update.html",msg=msg)
    
if __name__ == '__main__':
    app.run(debug= True)
