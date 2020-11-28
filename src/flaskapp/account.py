from flask import (render_template,
                    request,
                    redirect,
                    url_for,
                    session)
from flaskapp import app,dbinterface

def create_account(id,pw,role):
    dbinterface.create_account(id,pw,role)

def signin(id,pw):
    t = dbinterface.signin(id,pw)
    if t!=None:
        user = {'id':t[0][0],'role':t[0][2]}
        session["user"]=user
        return user
    else:
        return None

def update_info(newinfo):
    dbinterface.update_account(get_id(),newinfo["id"])

def is_loggedin():
    return "user" in session

def signout():
    if is_loggedin():
        session.pop("user",None)

def get_id():
    if is_loggedin():
        return session["user"]["id"]
    else:
        return None

def get_role():
    if is_loggedin():
        return session["user"]["role"]
    else:
        return None

def is_admin():
    return get_role()=="admin"

def get_session():
    if is_loggedin():
        return session["user"]
    else:
        return None

