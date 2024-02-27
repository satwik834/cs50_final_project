from flask import Flask, render_template,request,redirect,url_for,session,jsonify
from helpers import *
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'BAD_SECRET_KEY'


@app.route("/", methods = ["GET"] )
@login_required
def index():
        todos = get_todos(session["user_id"][0][0])
        return render_template("index.html",todos = todos,email = session["email"])
    
    

    


@app.route("/login", methods = ["GET","POST"] )
def login():
    session.clear()

    if request.method == "GET":
        return render_template("login.html",message="what the fuck")
    if request.method == "POST":
         email  = request.form.get("email")
         password = request.form.get("password")
         logged_in = signin(email,password)
         if logged_in:
             session["email"] = email
             session["user_id"] = get_userid(email)
             return redirect("/")
         else:
            return render_template("login.html", messasge= "invalid email or password")
         
        
         


@app.route("/register", methods = ["GET","POST"] )
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmpassword")
        hashed_password = generate_password_hash(password)

        if(email == '' or password =='') :
             return render_template("register.html",message = 'email or password is missing')


        if password !=confirmation:
            return render_template("register.html",message = 'passwords do not match')
        created = signup(email,hashed_password)


        return render_template("register.html",message = created)
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")




@app.route("/addtodo", methods = ['POST'])
@login_required
def todo():
    data = request.get_json()
    task = data.get('task')
    id = 8
    id = session["user_id"][0][0]
    #change 8 to the user id of the logged in user
    add_todo(id,task)   
    return jsonify({'message': 'Task added successfully'}),200




@app.route("/deletetodo",methods = ['POST'])
@login_required
def delete():
    data = request.get_json()
    task = data.get('task')
    id = session["user_id"][0][0]
    deleted = delete_todo(id,task)
    if deleted:
        return jsonify({'message': 'Task removed successfully'}),200
    else:
        return jsonify({'message': 'An error occurred'}), 500
    



if __name__ == '__main__':
    app.run(debug=True)



#https://github.com/thisbejim/Pyrebase#database pyrebase docs  
# pallette https://colorhunt.co/palette/d2e0fbf9f3ccd7e5ca8eaccd

