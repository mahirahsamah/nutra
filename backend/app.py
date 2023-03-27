from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/capstone'
db = SQLAlchemy(app)

class Custom(db.Model):
    itemID = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Custom: {self.itemName}"

    def __init__(self, itemName):
        self.itemName = itemName
# class Custom(db.Model):
#     itemID = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.Float, nullable=False)
#     score = db.Column(db.Float, nullable=True)
#     fatTot = db.Column(db.Float, nullable=True)
#     fatSat = db.Column(db.Float, nullable=True)
#     fatTrans = db.Column(db.Float, nullable=True)
#     cholesterol = db.Column(db.Float, nullable=True)
#     sodium = db.Column(db.Float, nullable=True)
#     potassium = db.Column(db.Float, nullable=True)
#     carbTot = db.Column(db.Float, nullable=True)
#     dietaryFiber = db.Column(db.Float, nullable=True)
#     sugar = db.Column(db.Float, nullable=True)
#     protein = db.Column(db.Float, nullable=True)
#     vitA = db.Column(db.Float, nullable=True)
#     vitC = db.Column(db.Float, nullable=True)
#     calories = db.Column(db.Float, nullable=True)
#     iron = db.Column(db.Float, nullable=True)
    
#     def __repr__(self):
#         return f"Custom: {self.itemID}"

#     def __init__(self, price, score, fatTot, fatSat, fatTrans, cholesterol, sodium, potassium, 
#                  carbTot, dietaryFiber, sugar, protein, vitA, vitC, calories, iron):
#         self.price = price 
#         self.score = score
#         self.fatTot = fatTot
#         self.fatSat = fatSat
#         self.fatTrans = fatTrans
#         self.cholesterol = cholesterol
#         self.sodium = sodium
#         self.potassium = potassium 
#         self.carbTot = carbTot
#         self.dietaryFiber = dietaryFiber
#         self.sugar = sugar
#         self.protein = protein
#         self.vitA = vitA
#         self.vitC = vitC
#         self.calories = calories
#         self.iron = iron
        
# class User(db.Model):
#     userID = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, nullable=False)
#     password = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, nullable=True)
#     vegetarian = db.Column(db.Boolean, nullable=True)
#     vegan = db.Column(db.Boolean, nullable=True)
#     halal = db.Column(db.Boolean, nullable=True)
#     kosher = db.Column(db.Boolean, nullable=True)
#     glutenFree = db.Column(db.Boolean, nullable=True)
#     lactoseInt = db.Column(db.Boolean, nullable=True)
#     lowSodium = db.Column(db.Boolean, nullable=True)
#     lowCarb = db.Column(db.Boolean, nullable=True)
#     highProtien = db.Column(db.Boolean, nullable=True)
#     keto = db.Column(db.Boolean, nullable=True)
#     mushrooms = db.Column(db.Boolean, nullable=True)
#     seafood = db.Column(db.Boolean, nullable=True)
#     pickles = db.Column(db.Boolean, nullable=True)
    
#     def __repr__(self):
#         return f"Event: {self.userID}"

#     def __init__(self, price, score, fatTot, fatSat, fatTrans, cholesterol, sodium, potassium, 
#                  carbTot, dietaryFiber, sugar, protein, vitA, vitC, calories, iron):
#         self.price = price 
#         self.score = score
#         self.fatTot = fatTot
#         self.fatSat = fatSat
#         self.fatTrans = fatTrans
#         self.cholesterol = cholesterol
#         self.sodium = sodium
#         self.potassium = potassium 
#         self.carbTot = carbTot
#         self.dietaryFiber = dietaryFiber
#         self.sugar = sugar
#         self.protein = protein
#         self.vitA = vitA
#         self.vitC = vitC
#         self.calories = calories
#         self.iron = iron
    
@app.route('/')
def home():
    return "Test Page"


@app.route('/dummy')
def dummy():
    return {"custom": ["custom1", "custom2", "custom3"]}

if __name__ == '__main__':
    app.run()
