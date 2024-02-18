import sqlite3
from werkzeug.security import check_password_hash
from flask import session,redirect
from functools import wraps


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
    return False

def get_todos(id : int):
    connection  = sqlite3.connect("static\database.db")
    db = connection.cursor()
    db.execute("SELECT text FROM todos WHERE user_id = ?",(id,))
    todos = db.fetchall()
    return todos

def add_todo(id,text):
    
    connection = sqlite3.connect("static\database.db")
    db = connection.cursor()
    db.execute("INSERT INTO todos(user_id,text) VALUES(?,?) ",(id,text))
    connection.commit()   

def delete_todo(id,text):
    try:
        connection = sqlite3.connect("static/database.db")
        db = connection.cursor()

        db.execute("DELETE FROM todos WHERE user_id = ? AND text = ?",(id,text))
        connection.commit()

        return True
    except sqlite3.error as e:
        print(e)
        return False
    finally:
        connection.close()                                                    




def get_userid(email):
    connection  = sqlite3.connect("static\database.db")
    db = connection.cursor()
    db.execute("SELECT user_id FROM users WHERE email = ?",(email))
    id = db.fetchall()
    return id;

