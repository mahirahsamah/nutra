from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
from flask import jsonify
import json
import sqlalchemy
from sqlalchemy import create_engine, text
import os
import pprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/capstone'
db = SQLAlchemy(app)
engine = create_engine('postgresql://postgres:admin@localhost/capstone')
CORS(app)

# spoonacular api
#spoonacular_api_key = os.environ["SPOONACULAR_API_KEY"]
#spoon_url = ""

class User(db.Model):
    
    # user auth
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    # user body info
    gender = db.Column(db.String)
    weight_lbs = db.Column(db.Float)
    age = db.Column(db.Integer)
    height_feet = db.Column(db.Integer)
    height_inches = db.Column(db.Integer)
    activity_level=db.Column(db.String)

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
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    # def __init__(self, username, email, password, gender, weight_lbs, age, height_feet, height_inches, activity_level, vegitarian, vegan, halal, kosher, gluten_free, dairy_free, lactose_int, low_sodium, low_carb, high_protein, keto, paleo, preferences, restricitons):
    #     self.username = username
    #     self.email = email
    #     self.password = password
    #     self.gender = gender
    #     self.weight_lbs = weight_lbs
    #     self.age = age
    #     self.height_feet = height_feet
    #     self.height_inches = height_inches
    #     self.activity_level=activity_level
    #     self.vegitarian = vegitarian
    #     self.vegan = vegan
    #     self.halal = halal
    #     self.kosher = kosher
    #     self.gluten_free = gluten_free
    #     self.dairy_free = dairy_free
    #     self.lactose_int = lactose_int
    #     self.low_sodium = low_sodium
    #     self.low_carb = low_carb
    #     self.high_protein = high_protein
    #     self.keto = keto
    #     self.paleo = paleo
    #     self.preferences = preferences
    #     self.restrictions = restricitons
  
@app.route('/')
def home():
    return "Backend"


def format_user(user):
    return{
        "userID": user.userID,
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "gender": user.gender,
        "weight_lbs": user.weight_lbs,
        "age": user.age,
        "height_feet": user.height_feet,
        "height_inches": user.height_inches,
        "activity_level": user.activity_level,
        "vegitarian": user.vegitarian,
        "vegan": user.vegan,
        "halal": user.halal,
        "kosher": user.kosher,
        "gluten_free": user.gluten_free,
        "dairy_free": user.dairy_free,
        "lactose_int": user.lactose_int,
        "low_sodium": user.low_sodium,
        "low_carb": user.low_carb,
        "high_protein": user.high_protein,
        "keto": user.keto,
        "paleo": user.paleo,
        "preferences": user.preferences,
        "restrictions": user.restrictions
    }

# POST user information

# POST ALL
@app.route('/post_whole_user', methods=['POST'])
def post_whole_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    gender = request.json['gender']
    weight_lbs = request.json['weight_lbs']
    age = request.json['age']
    height_feet = request.json['height_feet']
    height_inches = request.json['height_inches']
    activity_level=request.json['activity_level']
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

    thisUser = User(username, email, password, gender, weight_lbs, age, height_feet,
                    height_inches, activity_level, vegitarian, vegan, halal, kosher, gluten_free, 
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

# Checks for user and password match, returns user if exist
@app.route('/checklogin', methods=['GET'])
def check_login():
    user = request.args.get('user')
    pss = request.args.get('pass')
    result = db.session.query(User).filter_by(username=user, password=pss)
    users = []
    for user in result:
        users.append(format_user(user))
    # formatted_user = format_user(result)
    return {'user': users}

# Creates account if username is unique
@app.route('/createuser', methods=['POST'])
def create_user():
    user = request.args.get('user')
    pss = request.args.get('pass')
    eml = request.args.get('email')

    result = db.session.query(User).filter_by(username=user)
    users = []
    for user in result:
        users.append(format_user(user))

    if(len(users) == 0):
        newUser = User(username= user,
                       password= pss,
                       email= eml)
        db.session.add(newUser)
        db.session.commit()
        return {'user': users}
    else:
        return {'user': users}
    
# Updates user
@app.route('/updateuser', methods=['PUT'])
def update_user():
    user = request.args.get('user')
    user = User.query.filter_by(username=user)
    user.update(dict())
    db.session.commit()
    return {'user': format_user(user.one())}

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



# get all users
@app.route('/get_users_info', methods=['GET'])
def get_events():
    events = User.query.order_by(User.userID.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_user(event))
    return {'events': event_list}

# get single user
@app.route('/get_user/<userID>', methods=['GET'])
def single_event(userID):
    event = User.query.filter_by(userID = userID).one()
    formatted_event = format_user(event)
    return {'event':formatted_event}

# delete an event
@app.route('/delete_user/<userID>', methods=['DELETE'])
def delete_event(userID):
    event = User.query.filter_by(userID=userID).one()
    db.session.delete(event)
    db.session.commit()
    return f'Event (id: {userID}) deleted.'

# edit a user -- NOT DONE
@app.route('/edit_user/<edit_column>/<userID>', methods=['PUT'])
def update_event(edit_column, userID):
    event = User.query.filter_by(userID=userID)
    to_edit = request.json[edit_column]
    #return to_edit
    event.update(dict(edit_column=to_edit))
    db.session.commit()
    return {'event':format_user(event.one())}



@app.route('/get_nutrition/<userID>', methods=['GET'])
#def nutrients_amounts(gender, weight_lbs, age, height_feet, height_inches, activity_level):
def nutrients_amounts(userID):
    energy = 0
    protein = 0
    fat = 0
    carbs = 0
    ree = 0

    calcium = 0
    iron = 0
    potassium = 0

    vitD = 0
    vitC = 0
    vitA = 0
    vitE = 0
    
    this_user = User.query.filter_by(userID = userID).one()
    #print(this_user.username)
    #return this_user.username
    
    # returns an array in the format: [kcals, protein, fat, carbs, ...]
    
    # protein
    # fats
    # carbohydrates
    # vitamins
    # minerals

    weight_kg = this_user.weight_lbs/2.20462262185
    height_cm = (this_user.height_feet + this_user.height_inches/12) * 30.48
    
    # MACROS
    # ree: resting energy expenditure
    if(this_user.gender=='male'):
        ree = (10*weight_kg) + (6.25*height_cm) - (5 * this_user.age) + 5
    elif(this_user.gender == 'female'):
        ree = (10*weight_kg) + (6.25*height_cm) - (5 * this_user.age) - 161
    #return [ree]
    # energy with activity level
    if(this_user.activity_level == 'sedentary'):
        energy = ree*1.2
    elif(this_user.activity_level == 'low'):
        energy = ree*1.375
    elif(this_user.activity_level == 'medium'):
        energy = ree*1.55
    elif(this_user.activity_level == 'high'):
        energy = ree*1.725
    
    #return [energy]
    # protein
    protein = this_user.weight_lbs * 0.825
    
    # fats
    fat = (0.3*energy)/9
    
    # carbs
    carbs = (energy - (protein*4) - (fat*9))/4
    
    # MICROS
    
    # in the format of: [energy, vitD(micrograms/d), vitC(micrograms/d), vitA(micrograms/d), vitE(mg/d), calcium (mg/d), iron(mg/d), potassium (mg/d)]
    
    if(this_user.age>=1 and this_user.age<=3):
        calcium = 700
        iron = 7
        potassium = 2000
    elif(this_user.age>3 and this_user.age<=8):
        calcium = 1000
        iron = 10
        potassium =2300
    else:
        if(this_user.gender=='male'):
            vitD = 15
            vitC = 90
            vitA = 900
            vitE = 15
            if(this_user.age>8 and this_user.age<=13):
                calcium = 1300
                iron = 8
                potassium =2500
            elif(this_user.age>13 and this_user.age <=18):
                calcium = 1300
                iron = 11
                potassium = 3000
            elif(this_user.age>18 and this_user.age <=30):
                calcium = 1000
                iron = 8
                potassium = 3400
            elif(this_user.age>30 and this_user.age <=50):
                calcium = 1000
                iron = 8
                potassium =3400
            elif(this_user.age>50 and this_user.age <=70):
                calcium = 1000
                iron = 8
                potassium =3400
            elif(this_user.age>70):
                calcium = 1200 
                iron = 8
                potassium =3400
            
            
        elif(this_user.gender=='female'):
            vitD = 15
            vitC = 75
            vitA = 700
            vitE = 15
            if(this_user.age>8 and this_user.age<=13):
                calcium = 1300
                iron = 8
                potassium = 2300
            elif(this_user.age>13 and this_user.age <=18):
                calcium = 1300
                iron = 15
                potassium = 2300
            elif(this_user.age>18 and this_user.age <=30):
                calcium = 1000
                iron = 18
                potassium = 2600
            elif(this_user.age>30 and this_user.age <=50):
                calcium = 1000
                iron = 18
                potassium = 2600
            elif(this_user.age>50 and this_user.age <=70):
                calcium = 1200
                iron = 8
                potassium = 2600
            elif(this_user.age>70):
                calcium = 1200
                iron = 8
                potassium = 2600
    

    return [energy, protein, fat, carbs, vitD, vitC, vitA, vitE, calcium, iron, potassium]


@app.route('/get_preferences/<userID>', methods=['GET'])
def get_preferences(userID):
    this_user = User.query.filter_by(userID = userID).one()
    preferences = (this_user.preferences).split(',')
    return preferences

@app.route('/get_restrictions/<userID>', methods=['GET'])
def get_restrictions(userID):
    this_user = User.query.filter_by(userID = userID).one()
    restrictions = (this_user.restrictions).split(',')
    return restrictions

def get_grocery_list(userID):
    
    # one protein dish
    # one dish with vegetables
    # one rice/grains
    # one dairy

    # first find recipes by nutrients
    # then remove recipes with restrictions
    # then select recipes with preferences

    # then get recipes that 

    # may need to split up recipes for variety; do two or three get requests from spoonacular each with less parameters, then calculate each nutrients and do math until nutrients are satisfied
    
    # get recipes based on macros
    # select 2-3 recipes for each week
    # use recipe ID to see what nutrients each recipe has
    # fill in rest of the recipes

    nutrients_amounts = nutrients_amounts(userID)

    energy = nutrients_amounts[0]
    protein = nutrients_amounts[1]
    fat = nutrients_amounts[2]
    carbs = nutrients_amounts[3]
    vitD = nutrients_amounts[4]
    vitC = nutrients_amounts[5]
    vitA = nutrients_amounts[6]
    vitE = nutrients_amounts[7]
    calcium = nutrients_amounts[8]
    iron = nutrients_amounts[9]
    potassium = nutrients_amounts[10]

    spoon_get_macros = "https://api.spoonacular.com/recipes/findByNutrients?minProtein="+(protein-20)+"&maxProtein="+protein+"&minFat="+(fat-20)+"&maxFat="+fat+"&minCarbs="+(carbs-20)+"&maxCarbs="+carbs+"&minVitaminD="+(vitD-20)+"&maxVitaminD="+vitD+"&minVitaminC="+(vitC-20)+"&maxVitaminC="+vitC+"&minVitaminA="+(vitA-20)+"&maxVitaminA="+vitA+"&minVitaminE="+(vitE-20)+"&maxVitaminE="+vitE+"&minCalcium="+(calcium-20)+"&maxCalcium="+calcium+"&minIron="+(iron-20)+"&maxIron="+iron+"&minPotassium="+(potassium-20)+"&maxPotassium="+potassium+"&number=100"


if __name__ == '__main__':
    app.run()
