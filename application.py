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

'''
@app.route('/User')
def hello_world(message=None, data=None):
	nt = NT('data', 'href caption')
	temp = Bird.query.all()
	n1 = nt(str(temp[0]),str(temp[0]))
	
	n2 = nt(str(temp[1]),str(temp[1]))
	n3 = nt(str(temp[2]),str(temp[2]))
	n4 = nt(str(temp[3]),str(temp[3]))
	dat=(n1,n2,n2,n3,n4)
	#dat = str(User.query.all())
	return render_template('login.html', message='wilkommen', data=dat)

print Bed.query.all()
@app.route('/search', methods=['POST', 'GET'])
def search(data=None):
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    bed_type = request.args.get('bed_type', '')
    email = request.args.get('email', '')
    address = request.args.get('address', '')
    temp = Bed.query.all()
    nt = NT('name', 'bed_type', 'email', 'address')
    dat = None

    for item in temp:
        if item.bed_type == bed_type:
            dat.append((item.name,item.bed_type,item.email,item.address))
    #do query with those traits, return template with them

    return render_template('search.html', data=dat)
'''

@app.route('/index')
def view():

	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
