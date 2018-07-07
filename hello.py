from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<string:name>")
def hi(name):
    return f"<h1>Hello,{name}!</h1>"

@app.route('/html')
def render_html():
    return render_template('template.html')
