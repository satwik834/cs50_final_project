import sqlite3
from werkzeug.security import check_password_hash


def signup(email,password):
    connection  = sqlite3.connect("static\database.db")
    db = connection.cursor()
    try:
        db.execute("INSERT INTO users (email,password) VALUES (?,?) ",(email,password))
        connection.commit()
        return("account successfully created")
        print(password)
    except:
        return("email already exists")
    
def signin(email,password):
    connection  = sqlite3.connect("static\database.db")
    db = connection.cursor()
    db.execute("SELECT * FROM users WHERE email = ?",(email,))
    data = db.fetchall()
    stored_hash = data[0][2]
    if check_password_hash(stored_hash,password):
        return True
    else:
        return False






