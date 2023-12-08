from flask import Flask, render_template,request,redirect,url_for,session
from helpers import signup,signin
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'BAD_SECRET_KEY'


@app.route("/", methods = ["GET"] )
def index():
    if request.method == "GET":
        try:
            if session['email'] != None:
                return render_template("logged_in.html",email=session['email'])
        except:
            return render_template("index.html",)
    
    

    


@app.route("/login", methods = ["GET","POST"] )
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
         email  = request.form.get("email")
         password = request.form.get("password")
         logged_in = signin(email,generate_password_hash(password))
         if logged_in:
             session['email'] = email
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
        if password !=confirmation:
            return render_template("register.html",message = 'passwords do not match')
        created = signup(email,hashed_password)


        return render_template("register.html",message = created)
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")




@app.route("/todolist")
def todo():
    return render_template('todo.html')


#https://github.com/thisbejim/Pyrebase#database pyrebase docs  
# pallette https://colorhunt.co/palette/d2e0fbf9f3ccd7e5ca8eaccd

#TODO do not overcomplicate it show login and register if no user is logged in  show their email and logout if a user is logged in