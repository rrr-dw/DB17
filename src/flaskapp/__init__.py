from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = 'topsecretkey'


app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='rtrt'
app.config['MYSQL_DATABASE_DB']='flaskapp'

mysql = MySQL()
mysql.init_app(app)

from flaskapp import route
from flaskapp import dbinterface