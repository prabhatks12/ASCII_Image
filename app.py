from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data', methods=['GET', 'POST'])
def data():
    d=request.form["image"]
    print("received")
    print("d",d)
    return render_template("index.html")
