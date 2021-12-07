from typing import Mapping
from flask import Flask, render_template
from jinja2 import environment
import pymongo

app = Flask(__name__)

# Database
myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mymongodb = myclient['user_login_system']
collection = mymongodb['users']

# Routes
from user import routes


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
