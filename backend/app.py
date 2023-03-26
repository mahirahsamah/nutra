from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:11072000@localhost/capstone'
db = SQLAlchemy(app)


class Custom(db.Model):
    itemID = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Event:{self.price}"
    
    def __init__(self, price):
        self.price = price
    
@app.route('/nutrition')
def nutrients_amounts(gender, weight_lbs, age, height_feet, height_inches, activity_level, strength_training):
    # returns an array in the format: [kcals, protein, fat, carbs, ...]
    
    # protein
    # fats
    # carbohydrates
    # vitamins
    # minerals

    weight_kg = weight_lbs/2.20462262185
    height_cm = (height_feet + height_inches/12) * 30.48
    
    # MACROS
    # ree: resting energy expenditure
    if(gender=='M'):
        ree = (10*weight_kg) + (6.25*height_cm) - (5 * age) + 5
    elif(gender == "W"):
        ree = (10*weight_kg) + (6.25*height_cm) - (5 * age) - 161
    
    # energy with activity level
    if(activity_level == 'sedentary'):
        energy = ree*1.2
    elif(activity_level == 'light'):
        energy = ree*1.375
    elif(activity_level == 'moderate'):
        energy = ree*1.55
    elif(activity_level == 'high'):
        energy = ree*1.725
    
    # protein
    protein = weight_lbs * 0.825
    
    # fats
    fat = 0.3*energy
    
    # carbs
    carbs = (energy - (protein*4) - (fat*9))/4
    
    # MICROS
    
    # in the format of: [energy, vitD(micrograms/d), vitC(micrograms/d), vitA(micrograms/d), vitE(mg/d), calcium (mg/d), iron(mg/d), potassium (mg/d)]
    
    if(age>=1 and age<=3):
        calcium = 700
        iron = 7
        potassium = 2000
    elif(age>3 and age<=8):
        calcium = 1000
        iron = 10
        potassium =2300
    else:
        if(gender=='M'):
            vitD = 15
            vitC = 90
            vitA = 900
            vitE = 15
            if(age>8 and age<=13):
                calcium = 1300
                iron = 8
                potassium =2500
            elif(age>13 and age <=18):
                calcium = 1300
                iron = 11
                potassium = 3000
            elif(age>18 and age <=30):
                calcium = 1000
                iron = 8
                potassium = 3400
            elif(age>30 and age <=50):
                calcium = 1000
                iron = 8
                potassium =3400
            elif(age>50 and age <=70):
                calcium = 1000
                iron = 8
                potassium =3400
            elif(age>70):
                calcium = 1200 
                iron = 8
                potassium =3400
            
            
        elif(gender=="F"):
            vitD = 15
            vitC = 75
            vitA = 700
            vitE = 15
            if(age>8 and age<=13):
                calcium = 1300
                iron = 8
                potassium = 2300
            elif(age>13 and age <=18):
                calcium = 1300
                iron = 15
                potassium = 2300
            elif(age>18 and age <=30):
                calcium = 1000
                iron = 18
                potassium = 2600
            elif(age>30 and age <=50):
                calcium = 1000
                iron = 18
                potassium = 2600
            elif(age>50 and age <=70):
                calcium = 1200
                iron = 8
                potassium = 2600
            elif(age>70):
                calcium = 1200
                iron = 8
                potassium = 2600
    

    return [energy, vitD, vitC, vitA, vitE, calcium, iron, potassium]

@app.route('/')
def home():
    return "Test Page"


@app.route('/dummy')
def dummy():
    return {"custom": ["custom1", "custom2", "custom3"]}

def format_event(event):
    return{
        "id":event.itemID,
        "price":event.price
    }

#create an event
@app.route('/event', methods=['POST'])
def create_event():
    price = request.json['price']
    event = Custom(price)
    db.session.add(event)
    db.session.commit()
    return format_event(event)

# get all events
@app.route('/event', methods=['GET'])
def get_events():
    events = Custom.query.order_by(Custom.itemID.asc()).all()
    event_list = []
    for event in events:
        #print(event.itemID)
        event_list.append(format_event(event))
    return {'events': event_list}

# get single event
@app.route('/event/<itemID>', methods=['GET'])
def single_event(itemID):
    event = Custom.query.filter_by(itemID = itemID).one()
    formatted_event = format_event(event)
    return {'event':formatted_event}

#def delete an event
@app.route('/event/<itemID>', methods=['DELETE'])
def delete_event(itemID):
    event = Custom.query.filter_by(itemID=itemID).one()
    db.session.delete(event)
    db.session.commit()
    return f'Event (id: {itemID}) deleted.'


if __name__ == '__main__':
    app.run()
