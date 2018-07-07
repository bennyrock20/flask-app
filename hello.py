import datetime
from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


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

@app.route('/save', methods=["POST"])
def save():
    name = request.form.get("name")
    return render_template('saved.html', name = name)
