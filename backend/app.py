from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/capstone'
db = SQLAlchemy(app)

class Custom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Event: {self.price}"

    def __init__(self, price, score):
        self.price = price 
        self.score = score
    
@app.route('/')
def home():
    return "Test Page"


@app.route('/dummy')
def dummy():
    return {"custom": ["custom1", "custom2", "custom3"]}

if __name__ == '__main__':
    app.run()