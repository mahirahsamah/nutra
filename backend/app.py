from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/capstone'
db = SQLAlchemy(app)

class Custom(db.model):
    id = db.Column(db.interger, primary_key=True)

@app.route('/')
def home():
    return "Test Page"

if __name__ == '__main__':
    app.run()