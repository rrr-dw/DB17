from flask import (render_template,
                    request,
                    redirect,
                    url_for,
                    session)
from flaskapp import app,account,userinterface

@app.route('/')
def root():
    if not account.is_loggedin():
        return redirect(url_for("signin"))
    else:
        return userinterface.render_template_UI("main.html")

@app.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        account.signin(id,pw)
        if account.is_loggedin():
            return redirect(url_for("root"))
    elif account.is_loggedin():
        return redirect(url_for("root"))

    return userinterface.render_template_UI("signin.html")

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        role = request.form['role']
        account.create_account(id,pw,role)
        return redirect(url_for("signin"))
    elif account.is_loggedin():
        return redirect(url_for("root"))
    else:
        return userinterface.render_template_UI("signup.html")

@app.route('/signout')
def signout():
    account.signout()
    return redirect(url_for("root"))

@app.route('/myaccount', methods=['GET','POST'])
def myaccount():
    if request.method == 'POST':
        account.update_info(request.form)
        return redirect(url_for("root"))
    else:
        return userinterface.render_template_UI("myaccount.html")


@app.route('/user/<id>')
def user(id):
    return account.get_id()==id and "OK" or "NULL"


'''
pages for admin
'''
@app.route('/tskstat')
def tskstat():
    if not account.is_admin():
        return redirect(url_for("root"))
    return userinterface.render_template_UI("todo.html")

@app.route('/tskcreate')
def tskcreate():
    if not account.is_admin():
        return redirect(url_for("root"))
    return userinterface.render_template_UI("tskcreate.html")

@app.route('/tskmgmt')
def tskmgmt():
    if not account.is_admin():
        return redirect(url_for("root"))
    return userinterface.render_template_UI("todo.html")

@app.route('/usrmgmt')
def usrmgmt():
    if not account.is_admin():
        return redirect(url_for("root"))
    return userinterface.render_template_UI("usrmgmt.html")
