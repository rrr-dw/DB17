from flask import (render_template,
                    request,
                    redirect,
                    url_for,
                    session,
                    jsonify)
from flaskapp import app,mysql,account,userinterface


def create_account(id,pw,role):
    cur = mysql.get_db().cursor()
    cur.execute("insert into users(id,pw,role) values(%s,%s,%s)",(id,pw,role))
    mysql.get_db().commit()
    cur.close()

def update_account(id,newid):
    cur = mysql.get_db().cursor()
    cur.execute("update users set id=%s where id=%s",(newid,id))
    mysql.get_db().commit()
    cur.close()

def signin(id,pw):
    cur = mysql.get_db().cursor()
    result = cur.execute("select * from users where id=%s and pw=%s",(id,pw))
    if result >0:
        return cur.fetchall()
    else:
        return None

@app.route('/db/users/get', methods=['GET'])
def get_users():
    if not account.is_admin():
        return userinterface.render_template_error_UI(403)
    cur = mysql.get_db().cursor()
    cur.execute("select ID,Role from users")
    return jsonify(cur.fetchall())
