from flask import Flask
from flask import request
from flask import render_template
from flask import json
from collections import namedtuple as NT
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models.db'
db = SQLAlchemy(app)


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    img_path = db.Column(db.String(120), unique=True)


    def __init__(self, name, img_path):
        self.name = name
        self.img_path = img_path

@app.route('/index')
def view():

	return render_template('index.html')
	
@app.route('/create')
def view():

	return render_template('create.html')
	
@app.route('/show')
def view():

	return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)
