import datetime
from flask import Flask, render_template,request,redirect,url_for
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import select
from mysql.connector import IntegrityError

app = Flask(__name__)

engine = create_engine('mysql+mysqlconnector://root@localhost/db_name')
connection = engine.connect()



@app.route("/")
def index():
    stm = "SELECT * FROM `user` JOIN `group` ON group.id = user.group_id"
    users = connection.execute(stm).fetchall()
    return render_template('index.html', users= users)

@app.route('/save', methods=["POST"])
def save():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    group = request.form.get("group")
    metada = MetaData()
    user = Table('user',metada,autoload = True,autoload_with=engine)
    ins = user.insert().values(user_name=name, email_address=email,password=password,group_id=group)
    result = connection.execute(ins)
    print(result)
    return redirect(url_for('index'))


@app.route("/name/<string:name>")
def hi(name):
    return f"<h1>Hello,{name}!</h1>"

@app.route('/html')
def render_html():
    head_line= "Flask"
    return render_template('template.html', headline= head_line)

@app.route('/is-new-year')
def new_year():
    head_line= "Flask"
    now= datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    names = ["Alice","Jane","Diana"]
    return render_template('new_year.html', new_year= new_year, names = names)

@app.route("/more")
def more():
    return "heres more"

@app.route('/new')
def new():
    return render_template('forms.html')
