from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:11072000@localhost/capstone'
db = SQLAlchemy(app)
#CORS(app)

class User(db.Model):
    
    # user auth
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    # user dietary
    vegitarian = db.Column(db.Boolean)
    vegan = db.Column(db.Boolean)
    halal = db.Column(db.Boolean)
    kosher = db.Column(db.Boolean)
    gluten_free = db.Column(db.Boolean)
    dairy_free = db.Column(db.Boolean)
    lactose_int = db.Column(db.Boolean)
    low_sodium = db.Column(db.Boolean)
    low_carb = db.Column(db.Boolean)
    high_protein = db.Column(db.Boolean)
    keto = db.Column(db.Boolean)
    paleo = db.Column(db.Boolean)

    # user preferences
    preferences = db.Column(db.String)

    # user restrictions/allergies
    restrictions = db.Column(db.String)

    #def user_list(self):
    #    return [self.userID, self.username, self.email, self.password, self.vegitarian, self.vegan, self.halal, self.kosher, self.gluten_free, self.dairy_free, self.lactose_int, self.low_sodium, self.low_carb, self.high_protein, self.keto, self.paleo, self.preferences, self.restricitons]

    def __repr__(self):
        return f"User: {self.username}"
    
    def __init__(self, username, email, password, vegitarian, vegan, halal, kosher, gluten_free, dairy_free, lactose_int, low_sodium, low_carb, high_protein, keto, paleo, preferences, restricitons):
        self.username = username
        self.email = email
        self.password = password
        self.vegitarian = vegitarian
        self.vegan = vegan
        self.halal = halal
        self.kosher = kosher
        self.gluten_free = gluten_free
        self.dairy_free = dairy_free
        self.lactose_int = lactose_int
        self.low_sodium = low_sodium
        self.low_carb = low_carb
        self.high_protein = high_protein
        self.keto = keto
        self.paleo = paleo
        self.preferences = preferences
        self.restrictions = restricitons
  
@app.route('/')
def home():
    return "Test Page"


def format_user(user):
    return{
        "userID":user.userID,
        "username" :user.username
    }

# POST user information

# POST ALL
@app.route('/post_whole_user', methods=['POST'])
def post_whole_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    vegitarian = request.json['vegitarian']
    vegan = request.json['vegan']
    halal = request.json['halal']
    kosher = request.json['kosher']
    gluten_free = request.json['gluten_free']
    dairy_free = request.json['dairy_free']
    lactose_int = request.json['lactose_int']
    low_sodium = request.json['low_sodium']
    low_carb = request.json['low_carb']
    high_protein = request.json['high_protein']
    keto = request.json['keto']
    paleo = request.json['paleo']
    preferences = request.json['preferences']
    restrictions = request.json['restrictions']

    thisUser = User(username, email, password, vegitarian, vegan, halal, kosher, gluten_free, 
                    dairy_free, lactose_int, low_sodium, low_carb, high_protein,
                    keto, paleo, preferences, restrictions)
    
    db.session.add(thisUser)
    db.session.commit()
    return format_user(thisUser)

'''
{
    "username" :"mahirah",
    "email" :"mahirah@gmail.com",
    "password" :"examplepass",
    "vegitarian" :false,
    "vegan" :false,
    "halal" :true,
    "kosher" :false,
    "gluten_free" :false,
    "dairy_free" :false,
    "lactose_int" :false,
    "low_sodium" :false,
    "low_carb" :false,
    "high_protein" :false,
    "keto" :false,
    "paleo" :false,
    "preferences" :"chicken, brocolli",
    "restrictions" :"none"
}
'''

@app.route('/events', methods=['POST'])
def create_event1():
    username = request.json['username']
    event = User(username)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/username', methods=['POST'])
def create_event_username():
    username = request.json['username']
    event = User(username)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST email
@app.route('/email', methods=['POST'])
def create_event_email():
    email = request.json['email']
    event = User(email)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST password
@app.route('/password', methods=['POST'])
def create_event_password():
    password = request.json['password']
    event = User(password)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/vegitarian', methods=['POST'])
def create_event_vegitarian():
    vegitarian = request.json['vegitarian']
    event = User(vegitarian)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/vegan', methods=['POST'])
def create_event_vegan():
    vegan = request.json['vegan']
    event = User(vegan)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/halal', methods=['POST'])
def create_event_halal():
    halal = request.json['halal']
    event = User(halal)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST kosher
@app.route('/kosher', methods=['POST'])
def create_event_kosher():
    kosher = request.json['kosher']
    event = User(kosher)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/gluten_free', methods=['POST'])
def create_event_gluten_free():
    gluten_free = request.json['gluten_free']
    event = User(gluten_free)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/dairy_free', methods=['POST'])
def create_event_dairy_free():
    dairy_free = request.json['dairy_free']
    event = User(dairy_free)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/lactose_int', methods=['POST'])
def create_event_lactose_int():
    lactose_int = request.json['lactose_int']
    event = User(lactose_int)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/low_sodium', methods=['POST'])
def create_event_low_sodium():
    low_sodium = request.json['low_sodium']
    event = User(low_sodium)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/low_carb', methods=['POST'])
def create_event_low_carb():
    low_carb = request.json['low_carb']
    event = User(low_carb)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/high_protein', methods=['POST'])
def create_event_high_protein():
    high_protein = request.json['high_protein']
    event = User(high_protein)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

    # POST username
@app.route('/keto', methods=['POST'])
def create_event_keto():
    keto = request.json['keto']
    event = User(keto)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/paleo', methods=['POST'])
def create_event_paleo():
    paleo = request.json['paleo']
    event = User(paleo)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/preferences', methods=['POST'])
def create_event_preferences():
    preferences = request.json['preferences']
    event = User(preferences)
    db.session.add(event)
    db.session.commit()
    return format_user(event)

# POST username
@app.route('/restrictions', methods=['POST'])
def create_event_restrictions():
    restrictions = request.json['restrictions']
    event = User(restrictions)
    db.session.add(event)
    db.session.commit()
    return format_user(event)



# get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = User.query.order_by(User.itemID.asc()).all()
    event_list = []
    for event in events:
        #print(event.itemID)
        event_list.append(format_user(event))
    return {'events': event_list}

# get single event
@app.route('/events/<itemID>', methods=['GET'])
def single_event(itemID):
    event = User.query.filter_by(itemID = itemID).one()
    formatted_event = format_user(event)
    return {'event':formatted_event}

#def delete an event
@app.route('/events/<itemID>', methods=['DELETE'])
def delete_event(itemID):
    event = User.query.filter_by(itemID=itemID).one()
    db.session.delete(event)
    db.session.commit()
    return f'Event (id: {itemID}) deleted.'

# edit an event
@app.route('/events/<itemID>', methods=['PUT'])
def update_event(itemID):
    event = User.query.filter_by(itemID=itemID)
    price = request.json['price']
    event.update(dict(price=price))
    db.session.commit()
    return {'event':format_user(event.one())}


  
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



if __name__ == '__main__':
    app.run()
