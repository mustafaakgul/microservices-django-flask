from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

from flask_migrate import Migrate
#from flask_script import Manager

#terminal python3 main.py do see adter that close web server docker-compose up in 127.0.0.1:8001 in postman saw hello
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
CORS(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name = 'user_product_unique')


@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
