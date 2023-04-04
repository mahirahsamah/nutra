from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
import os
import pprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:11072000@localhost/capstone'
db = SQLAlchemy(app)
#CORS(app)

# spoonacular api
spoonacular_api_key = os.environ["SPOONACULAR_API_KEY"]
spoon_url = "https://api.spoonacular.com/recipes/findByNutrients"

class User(db.Model):
    
    # user auth
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
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
    
    def __init__(self, username, email, password, gender, weight_lbs, age, height_feet, height_inches, activity_level, vegitarian, vegan, halal, kosher, gluten_free, dairy_free, lactose_int, low_sodium, low_carb, high_protein, keto, paleo, preferences, restricitons):
        self.username = username
        self.email = email
        self.password = password
        self.gender = gender
        self.weight_lbs = weight_lbs
        self.age = age
        self.height_feet = height_feet
        self.height_inches = height_inches
        self.activity_level=activity_level
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
    
    calcium_ul = 0
    iron_ul = 0

    vitD = 0
    vitC = 0
    vitA = 0
    vitE = 0
    
    vitD_ul = 0
    vitC_ul = 0
    vitA_ul = 0
    vitE_ul = 0
    
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
        vitD = 15
        vitC = 15
        vitA = 300
        vitE = 6
        
        vitD_ul = 63
        vitC_ul = 400
        vitA_ul = 600
        vitE_ul = 200
            
        calcium = 700
        iron = 7
        potassium = 2000
        
        calcium_ul = 2500
        iron_ul = 40
        # NO potassium_ul
        
    elif(this_user.age>3 and this_user.age<=8):
        vitD = 15
        vitC = 25
        vitA = 400
        vitE = 7
        
        vitD_ul = 75
        vitC_ul = 650
        vitA_ul = 900
        vitE_ul = 300
        
        calcium = 1000
        iron = 10
        potassium =2300
        
        calcium_ul = 2500
        iron_ul = 40
        # NO potassium_ul
        
    else:
        if(this_user.gender=='male'):
            vitD = 15
            vitC = 90
            vitA = 900
            vitE = 15
            
            if(this_user.age>8 and this_user.age<=13):
                vitC = 45
                vitA = 600
                vitE = 11
                
                vitD_ul = 100
                vitC_ul = 1200
                vitA_ul = 1700
                vitE_ul = 600
                
                calcium = 1300
                iron = 8
                potassium =2500
                
                calcium_ul = 3000
                iron_ul = 40
                
            elif(this_user.age>13 and this_user.age <=18):
                vitC = 75
                
                vitD_ul = 100
                vitC_ul = 1800
                vitA_ul = 2800
                vitE_ul = 800
                
                calcium = 1300
                iron = 11
                potassium = 3000
                
                calcium_ul = 3000
                iron_ul = 45
                
            elif(this_user.age>18 and this_user.age <=30):
                vitD_ul = 100
                vitC_ul = 2000
                vitA_ul = 3000
                vitE_ul = 1000
                
                calcium = 1000
                iron = 8
                potassium = 3400
                
                calcium_ul = 2500
                iron_ul = 45
                
            elif(this_user.age>30 and this_user.age <=50):
                vitD_ul = 100
                vitC_ul = 2000
                vitA_ul = 3000
                vitE_ul = 1000
                
                calcium = 1000
                iron = 8
                potassium =3400
                
                calcium_ul = 2500
                iron_ul = 45
                
            elif(this_user.age>50 and this_user.age <=70):
                vitD_ul = 100
                vitC_ul = 2000
                vitA_ul = 3000
                vitE_ul = 1000
                
                calcium = 1000
                iron = 8
                potassium =3400
                
                calcium_ul = 2000
                iron_ul = 45
                
            elif(this_user.age>70):
                vitD_ul = 100
                vitC_ul = 2000
                vitA_ul = 3000
                vitE_ul = 1000
                
                vitD = 20
                
                calcium = 1200 
                iron = 8
                potassium =3400
                
                calcium_ul = 2000
                iron_ul = 45
            
            
        elif(this_user.gender=='female'):
            
            if(this_user.age>8 and this_user.age<=13):
                vitD = 15
                vitC = 45
                vitA = 600
                vitE = 11
                
                vitD_ul = 100
                vitC_ul = 1200
                vitA_ul = 1700
                vitE_ul = 600
                
                calcium = 1300
                iron = 8
                potassium = 2300
                
                calcium_ul = 3000
                iron_ul = 40
    
            elif(this_user.age>13 and this_user.age <=18):
                vitD = 15
                vitC = 65
                vitA = 700
                vitE = 15
                
                vitD_ul = 100
                vitC_ul = 1800
                vitA_ul = 2800
                vitE_ul = 800
                
                calcium = 1300
                iron = 15
                potassium = 2300
                
                calcium_ul = 3000
                iron_ul = 45
                
            elif(this_user.age>18 and this_user.age <=30):
                vitD = 15
                vitC = 65
                vitA = 700
                vitE = 15
                
                vitD_ul = 100
                vitC_ul = 2000
                vitA_ul = 3000
                vitE_ul = 1000
                
                calcium = 1000
                iron = 18
                potassium = 2600
                
                calcium_ul = 2500
                iron_ul = 45
                
            elif(this_user.age>30 and this_user.age <=50):
                vitD = 15
                vitC = 65
                vitA = 700
                vitE = 15
                
                vitD_ul = 100
                vitC_ul = 2000
                vitA_ul = 3000
                vitE_ul = 1000
                
                calcium = 1000
                iron = 18
                potassium = 2600
                
                calcium_ul = 2500
                iron_ul = 45
                
            elif(this_user.age>50 and this_user.age <=70):
                vitD = 15
                vitC = 65
                vitA = 700
                vitE = 15
                
                vitD_ul = 100
                vitC_ul = 2000
                vitA_ul = 3000
                vitE_ul = 1000
                
                calcium = 1200
                iron = 8
                potassium = 2600
                
                calcium_ul = 2000
                iron_ul = 45
                
            elif(this_user.age>70):
                vitD = 20
                vitC = 65
                vitA = 700
                vitE = 15
                
                vitD_ul = 100
                vitC_ul = 2000
                vitA_ul = 3000
                vitE_ul = 1000
                
                calcium = 1200
                iron = 8
                potassium = 2600
                
                calcium_ul = 2000
                iron_ul = 45
    

    return [energy, protein, fat, carbs, vitD, vitC, vitA, vitE, calcium, iron, potassium, vitD_ul, vitC_ul, vitA_ul, vitE_ul, calcium_ul, iron_ul]


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
    
    # ULs
    vitD_ul = nutrients_amounts[11]
    vitC_ul = nutrients_amounts[12]
    vitA_ul = nutrients_amounts[13]
    vitE_ul = nutrients_amounts[14]
    calcium_ul = nutrients_amounts[15]
    iron_ul = nutrients_amounts[16]
    
    preferences = get_preferences(userID)
    restriction = get_restrictions(userID)

    spoon_get_macros = "https://api.spoonacular.com/recipes/findByNutrients?minProtein="+(protein-20)+"&maxProtein="+(protein+20)+"&minFat="+(fat-20)+"&maxFat="+(fat+20)+"&minCarbs="+(carbs-20)+"&maxCarbs="+(carbs+20)+"&minVitaminD="+(vitD-20)+"&maxVitaminD="+((vitD+vitD_ul)/2)+"&minVitaminC="+(vitC-20)+"&maxVitaminC="+((vitC+vitC_ul)/2)+"&minVitaminA="+(vitA-20)+"&maxVitaminA="+((vitA+vitA_ul)/2)+"&minVitaminE="+(vitE-20)+"&maxVitaminE="+((vitE+vitE_ul)/2)+"&minCalcium="+(calcium-20)+"&maxCalcium="+((calcium+calcium_ul)/2)+"&minIron="+(iron-20)+"&maxIron="+((iron+iron_ul)/2)+"&minPotassium="+(potassium-20)+"&maxPotassium="+(potassium+20)+"&number=100"


if __name__ == '__main__':
    app.run()
