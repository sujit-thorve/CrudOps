from flask import Flask, render_template,request,redirect,session,url_for
import sqlite3
app= Flask(__name__)
#hello this is change
app.secret_key = "123"
@app.route("/", methods = ['GET' , 'POST'])
def home():
    msg= None
    if(request.method == "POST"):
       if(request.form["name"] !="" and request.form["username"] !="" and request.form["password"] !=""):
           username = request.form["username"]
           name = request.form["name"]
           password = request.form["password"]
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
         name = request.form["nm"]
         if( name =="" ):
             msg = "please enter username"
             print(name)
         else :
             conn= sqlite3.connect("signup.db")
             c = conn.cursor()
             print(name)
             c.execute("SELECT * FROM db1 WHERE username = '"+name+"' ")
             r = c.fetchall()
             print(r)
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
         name = request.form["nm"]
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
         uname = request.form["nm"]
         name = request.form["name"]
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
