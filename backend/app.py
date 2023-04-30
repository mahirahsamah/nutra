from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship 
from flask_cors import CORS
import requests
import json
import time
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/capstone'
db = SQLAlchemy(app)
CORS(app)

# spoonacular api key
api_key = "13cc54269ca54d258cf7b07e4383154c"

class User(db.Model):

    __tablename__ = 'users_table'
    __table_args__ = {'schema': 'public'}
    
    nutrition = relationship("UserNutrition")
    grocery_lists = relationship("GroceryLists")

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
    vegetarian = db.Column(db.Boolean)
    vegan = db.Column(db.Boolean)
    gluten_free = db.Column(db.Boolean)
    keto = db.Column(db.Boolean)
    paleo = db.Column(db.Boolean)
    pescetarian = db.Column(db.Boolean)

    # user preferences
    preferences = db.Column(db.String)

    # user restrictions/allergies
    restrictions = db.Column(db.String)

    def __repr__(self):
        return f"User: {self.username}"
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
#     def __init__(self, username, email, password, gender, weight_lbs, age, height_feet, height_inches, activity_level, vegetarian, vegan, gluten_free, keto, paleo, pescetarian, preferences, restricitons):
#         self.username = username
#         self.email = email
#         self.password = password
#         self.gender = gender
#         self.weight_lbs = weight_lbs
#         self.age = age
#         self.height_feet = height_feet
#         self.height_inches = height_inches
#         self.activity_level=activity_level
#         self.vegetarian = vegetarian
#         self.vegan = vegan
#         self.gluten_free = gluten_free
#         self.keto = keto
#         self.paleo = paleo
#         self.pescetarian = pescetarian
#         self.preferences = preferences
#         self.restrictions = restricitons
  

class UserNutrition(db.Model):

    __tablename__ = 'users_nutrition_table'
    __table_args__ = {'schema': 'public'}
    nutritionID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('public.users_table.userID'))
    #user_nutrition = relationship("User")


    energy = db.Column(db.Float)
    protein = db.Column(db.Float)
    fat = db.Column(db.Float)
    carbs = db.Column(db.Float)

    calcium = db.Column(db.Float)
    iron = db.Column(db.Float)
    potassium = db.Column(db.Float)
    
    calcium_ul = db.Column(db.Float)
    iron_ul = db.Column(db.Float)

    vitD = db.Column(db.Float)
    vitC = db.Column(db.Float)
    vitA = db.Column(db.Float)
    vitE = db.Column(db.Float)
    
    vitD_ul = db.Column(db.Float)
    vitC_ul = db.Column(db.Float)
    vitA_ul = db.Column(db.Float)
    vitE_ul = db.Column(db.Float)

    def __repr__(self):
        return f"User: {self.userID}"
    
    def __init__(self, userID, energy, protein, fat, carbs, calcium, iron, potassium, calcium_ul, iron_ul, vitA, vitD,vitC,vitE, vitA_ul, vitD_ul,vitC_ul,vitE_ul):
        self.userID = userID
        self.energy = energy
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.calcium = calcium
        self.iron = iron
        self.potassium = potassium
        self.calcium_ul=calcium_ul
        self.iron_ul = iron_ul
        self.vitA = vitA
        self.vitD = vitD
        self.vitC = vitC
        self.vitE = vitE
        self.vitA_ul = vitA_ul
        self.vitD_ul = vitD_ul
        self.vitC_ul = vitC_ul
        self.vitE_ul = vitE_ul


class WeeklyRecipes(db.Model):
    __tablename__ = 'users_weekly_recipes_table'
    __table_args__ = {'schema': 'public'}

    grocery_lists = relationship("GroceryLists")

    week_number_ID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('public.users_table.userID'))
    recipeIDs = db.Column(db.String) # this is a string of comma-separated recipe IDs

    def __repr__(self):
        return f"User: {self.userID}"
    
    def __init__(self, userID, recipeIDs):
        self.userID = userID
        self.recipeIDs = recipeIDs


class Latency(db.Model):
    __tablename__ = 'latency_table'
    __table_args__ = {'schema': 'public'}

    function_id = db.Column(db.Integer, primary_key=True)
    function_name = db.Column(db.String)
    time_taken_s = db.Column(db.Float)

    def __repr__(self):
        return f"Function ID: {self.function_id}"
    
    def __init__(self, function_name, time_taken_s):
        self.function_name = function_name
        self.time_taken_s = time_taken_s

class GroceryLists(db.Model):
    __tablename__ = 'grocery_lists_table'
    __table_args__ = {'schema': 'public'}

    listID = db.Column(db.Integer, primary_key=True)
    week_number_ID = db.Column(db.Integer, db.ForeignKey('public.users_weekly_recipes_table.week_number_ID'))
    userID = db.Column(db.Integer, db.ForeignKey('public.users_table.userID'))
    grocery_list = db.Column(db.String)


    def __repr__(self):
        return f"List ID: {self.listID}"
    
    def __init__(self, userID, week_number_ID, grocery_list):
        self.userID = userID
        self.week_number_ID = week_number_ID
        self.grocery_list = grocery_list

@app.route('/groceries')
def home():
    return "Test Page"


@app.route('/post_recipes', methods=['POST'])
def post_recipes():
    userID = request.args.get('userID')
    recipe_string= request.args.get('recipe_string')
    recipes = WeeklyRecipes(userID, recipe_string)

    db.session.add(recipes)
    db.session.commit()
    return "recipe " + recipe_string + " added to " + userID

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
        "vegetarian": user.vegetarian,
        "vegan": user.vegan,
        "gluten_free": user.gluten_free,
        "keto": user.keto,
        "paleo": user.paleo,
        "pescetarian":user.pescetarian,
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
    vegetarian = request.json['vegetarian']
    vegan = request.json['vegan']
    gluten_free = request.json['gluten_free']
    keto = request.json['keto']
    paleo = request.json['paleo']
    pescetarian = request.json['pescetarian']
    preferences = request.json['preferences']
    restrictions = request.json['restrictions']

    thisUser = User(username, email, password, gender, weight_lbs, age, height_feet,
                    height_inches, activity_level, vegetarian, vegan, gluten_free, keto, paleo, pescetarian, preferences, restrictions)
    
    db.session.add(thisUser)
    db.session.commit()
    return format_user(thisUser)

'''
{
    "username" :"mahirah",
    "email" :"mahirah@gmail.com",
    "password" :"examplepass",
    "gender": "female",
    "weight_lbs" : 126,
    "age" : 30,
    "height_feet" :5,
    "height_inches" :5,
    "activity_level":"low",
    "vegetarian" : false,
    "vegan" : false,
    "gluten_free" : true,
    "keto" : false,
    "paleo" : false,
    "pescetarian": true,
    "preferences" :"chicken, brocolli",
    "restrictions" :"none"
}
'''



# Checks for user and password match, returns user if exist
@app.route('/checklogin', methods=['GET'])
def check_login():
    user = request.args.get('user')
    pss = request.args.get('pass')
    result = User.query.filter_by(username=user, password=pss)
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

    result = User.query.filter_by(username=user)
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
    
# Returns requsted user from username
@app.route('/getuserinfo', methods=['GET'])
def get_user_info():
    user = request.args.get('user')
    result = User.query.filter_by(username=user)
    users = []
    for user in result:
        users.append(format_user(user))
    # formatted_user = format_user(result)
    return {'user': users}
    
# Updates user
@app.route('/updateuser', methods=['PUT'])
def update_user():
    user = request.args.get('user')
    gender = request.args.get('gender')
    weight_lbs = request.args.get('weight_lbs')
    age = request.args.get('age')
    height_feet = request.args.get('height_feet')
    height_inches = request.args.get('height_inches')
    activity_level = request.args.get('activity_level')
    vegetarian = request.args.get('vegetarian').capitalize()
    vegan = request.args.get('vegan').capitalize()
    gluten_free = request.args.get('gluten_free').capitalize()
    keto = request.args.get('keto').capitalize()
    paleo = request.args.get('paleo').capitalize()
    pescetarian = request.args.get('pescetarian').capitalize()
    preferences = request.args.get('preferences')
    restrictions = request.args.get('restrictions')

       

    user = User.query.filter_by(username=user)
    user.update(dict(
                    gender = gender, 
                    weight_lbs = weight_lbs,
                    age = age,
                    height_feet = height_feet,
                    height_inches = height_inches, 
                    activity_level = activity_level, 
                    vegetarian = eval(vegetarian), 
                    vegan = eval(vegan),
                    gluten_free = eval(gluten_free), 
                    keto = eval(keto), 
                    paleo = eval(paleo), 
                    pescetarian = eval(pescetarian),
                    preferences = preferences, 
                    restrictions = restrictions
                    ))
    db.session.commit()
    return {'user': format_user(user.one())}

@app.route('/updatelink', methods=['PUT'])
def update_link():
    return 1




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

@app.route('/get_nutrition/<userID>', methods=['GET', 'POST'])
#def nutrients_amounts(gender, weight_lbs, age, height_feet, height_inches, activity_level):
def get_nutrition(userID):
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
    
    return_list = [energy, protein, fat, carbs, vitD, vitC, vitA, vitE, calcium, iron, potassium, vitD_ul, vitC_ul, vitA_ul, vitE_ul, calcium_ul, iron_ul]
    #print(type(protein))
     
    nutrition_info = {"energy":energy, "protein":protein, "fat": fat, "carbs": carbs, "vitD": vitD, "vitC": vitC, "vitA": vitA, "vitE": vitE, "calcium": calcium, "iron": iron, "potassium": potassium, "vitD_ul":vitD_ul, "vitC_ul":vitC_ul, "vitA_ul":vitA_ul, "vitE_ul":vitE_ul, "calcium_ul":calcium_ul, "iron_ul":iron_ul}

    # post information to nutrition table in db
    user_nutrition = UserNutrition(userID, energy, protein, fat, carbs, calcium, iron, potassium, calcium_ul, iron_ul, vitA, vitD,vitC,vitE, vitA_ul, vitD_ul,vitC_ul,vitE_ul)
    
    db.session.add(user_nutrition)
    db.session.commit()

    return nutrition_info
    #return {"nutrients":return_list}


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

@app.route('/get_recipe_list/<userID>', methods=['GET'])
def get_recipe_list(userID):
    # time start for function
    # time is in seconds
    start_time = time.time()
    
    # get restrictions and preferences
    this_user = User.query.filter_by(userID = userID).one()
    preferences = (this_user.preferences).split(',')
    restrictions = (this_user.restrictions).split(',')
    
    includes = "&includeIngredients="+this_user.preferences.replace(" ", "")
    excludes = "&excludeIngredients="+this_user.restrictions.replace(" ", "")
    
    
    # make an array of all user diet info
    # in this format: [vegetarian, vegan, halal, kosher, gluten_free, dairy_free, lactose_int, low_sodium, low_carb, high_protein, keto, paleo]
    diet_string ="&diet="
    diet_types=""
    if this_user.gluten_free:
        diet_types+=",gluten free"
    if this_user.vegan:
        diet_types+=",vegan"
    if this_user.keto:
        diet_types+=",ketogenic"
    if this_user.vegetarian:
        diet_types+=",vegetarian"
    if this_user.paleo:
        diet_types+=",paleo"
    if this_user.pescetarian:
        diet_types+=",pescetarian"
        
    diet_string+=diet_types[1:]
    
   #user_diet = [this_user.vegetarian, this_user.vegan, this_user.halal, this_user.kosher, this_user.gluten_free, this_user.dairy_free, this_user.lactose_int, this_user.low_sodium, this_user.low_carb, this_user.high_protein, this_user.keto, this_user.paleo]
    
    nutrients_response = requests.get(f'http://localhost:5000/get_nutrition/{userID}')
    nutrients_amounts = nutrients_response.json()

    # first find recipes by nutrients
    # then remove recipes with restrictions
    # then select recipes with preferences

    # then get recipes that 

    # may need to split up recipes for variety; do two or three get 
    # requests from spoonacular each with less parameters, then 
    # calculate each nutrients and do math until nutrients are satisfied
    
    # get recipes based on macros & preferences
    # select 2-3 recipes for each week
    # use recipe ID to see what nutrients each recipe has
    # fill in rest of the recipes

    #nutrients_amounts = nutrients_amounts(userID)

    energy = str(nutrients_amounts['energy'])
    protein = str(nutrients_amounts['protein'])
    fat = str(nutrients_amounts['fat'])
    carbs = str(nutrients_amounts['carbs'])
    vitD = str(nutrients_amounts['vitD'])
    vitC =str(nutrients_amounts['vitC'])
    vitA = str(nutrients_amounts['vitA'])
    vitE = str(nutrients_amounts['vitE'])
    calcium = str(nutrients_amounts['calcium'])
    iron = str(nutrients_amounts['iron'])
    potassium = str(nutrients_amounts['potassium'])

    # ULs
    vitD_ul = str(nutrients_amounts['vitD_ul'])
    vitC_ul = str(nutrients_amounts['vitC_ul'])
    vitA_ul = str(nutrients_amounts['vitA_ul'])
    vitE_ul = str(nutrients_amounts['vitE_ul'])
    calcium_ul = str(nutrients_amounts['calcium_ul'])
    iron_ul = str(nutrients_amounts['iron_ul'])
    
    preferences = get_preferences(userID)
    restriction = get_restrictions(userID)
    
    find_by_nutrients_url = "https://api.spoonacular.com/recipes/complexSearch"

    # divide nutrients by 2 to account for lunch and dinner meals
    
    # ingredient preferences are randomized, includes will be added less than 20% of the time due to how much it limits the results
    if(random.random() <= 0.2):
        macros_query_params = "apiKey=" + api_key + "&minProtein="+str(float(protein)/2-20)+"&maxProtein="+str(float(protein)/2+20)+"&minFat="+str(float(fat)/2-20)+"&maxFat="+str(float(fat)/2+20)+"&minCarbs="+str(float(carbs)/2-20)+"&maxCarbs="+str(float(carbs)/2+20)+diet_string+includes+excludes+"&type=main course"
    else:
        macros_query_params = "apiKey=" + api_key + "&minProtein="+str(float(protein)/2-20)+"&maxProtein="+str(float(protein)/2+20)+"&minFat="+str(float(fat)/2-20)+"&maxFat="+str(float(fat)/2+20)+"&minCarbs="+str(float(carbs)/2-20)+"&maxCarbs="+str(float(carbs)/2+20)+diet_string+excludes+"&type=main course"
    
    # having the micronutrients in the query params makes it more constricting. so i am just going to let the user choose from list of recipes and then fill the rest of the nutrients in with snacks

    macros_query =  find_by_nutrients_url + "?" + macros_query_params 
    print(macros_query)
    macros_response = requests.get(macros_query)

    # time end for function
    end_time = time.time()
    total_time = end_time - start_time

    time_taken = Latency("generate_recipes", total_time)
    db.session.add(time_taken)
    db.session.commit()


    return macros_response.json()

# just run this one function when user selects their recipes 
@app.route('/get_remaining_ingredients/<userID>/<weekID>', methods=['GET','PUT','POST']) # this function gets remaining ingredients AND posts the final grocery list to the db
def get_remaining_ingredients(userID, weekID):
    # time start for function
    # time is in seconds
    start_time = time.time()


    this_user = User.query.filter_by(userID = userID).one()
    preferences = (this_user.preferences).split(',')
    restrictions = (this_user.restrictions).split(',')
    
    includes = "&includeIngredients="+this_user.preferences.replace(" ", "")
    excludes = "&excludeIngredients="+this_user.restrictions.replace(" ", "")

    diet_string ="&diet="
    diet_types=""
    if this_user.gluten_free:
        diet_types+=",gluten free"
    if this_user.vegan:
        diet_types+=",vegan"
    if this_user.keto:
        diet_types+=",ketogenic"
    if this_user.vegetarian:
        diet_types+=",vegetarian"
    if this_user.paleo:
        diet_types+=",paleo"
    if this_user.pescetarian:
        diet_types+=",pescetarian"
        
    diet_string+=diet_types[1:]

    # get recipes IDs from the weekly recipes table
    recipe_ids = WeeklyRecipes.query.filter_by(userID = userID, week_number_ID = weekID).one()
    recipes = (recipe_ids.recipeIDs.replace(" ", "")).split(',')

    micronutrients = UserNutrition.query.filter_by(userID = userID).one()

    energy = str(micronutrients.energy)

    vitD = str(micronutrients.vitD)
    vitC =str(micronutrients.vitC)
    vitA = str(micronutrients.vitA)
    vitE = str(micronutrients.vitE)
    calcium = str(micronutrients.calcium)
    iron = str(micronutrients.iron)
    potassium = str(micronutrients.potassium)

    # ULs
    vitD_ul = str(micronutrients.vitD_ul-10)
    vitC_ul = str(micronutrients.vitC_ul-200)
    vitA_ul = str(micronutrients.vitA_ul-300)
    vitE_ul = str(micronutrients.vitE_ul-100)
    calcium_ul = str(micronutrients.calcium_ul - 200)
    iron_ul = str(micronutrients.iron_ul - 5)

    # total nutrition (sum) from recipes
    energy_sum = 0
    vitD_sum = 0
    vitC_sum =0
    vitA_sum = 0
    vitE_sum = 0
    calcium_sum =0 
    iron_sum = 0
    potassium_sum = 0

    # one json object to hold all the nutrients in all the recipes
    recipe_nutrition_info_json = {}

    # get nutrients of all the recipe IDs
    for recipe in recipes:
        recipe_nutrients_url = f"https://api.spoonacular.com/recipes/{recipe}/nutritionWidget.json?apiKey={api_key}"
        response = requests.get(recipe_nutrients_url)
        recipe_nutrition_info_json[recipe]=response.json()
        
        energy_sum += float(recipe_nutrition_info_json[str(recipe)]["bad"][0]["amount"])

        for i in range(len(recipe_nutrition_info_json[str(recipe)]["good"])):
        
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Calcium":
                calcium_sum += float(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin C":
                vitC_sum += float(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin A":
                vitA_sum += float(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin E":
                vitE_sum += float(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin D":
                vitD_sum += float(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin D":
                iron_sum += float(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin D":
                potassium_sum += float(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
        
    # remaining nutrients
    energy_remaining = round(float(energy) - float(energy_sum), 2)
    vitD_remaining = round(float(vitD) - float(vitD_sum), 2)
    vitC_remaining = round(float(vitC) - float(vitC_sum), 2)
    vitA_remaining = round(float(vitA) - float(vitA_sum), 2)
    vitE_remaining = round(float(vitE) - float(vitE_sum), 2)
    calcium_remaining = round(float(calcium) - float(calcium_sum), 2)
    iron_remaining = round(float(iron) - float(iron_sum), 2)
    potassium_remaining = round(float(potassium) - float(potassium_sum), 2)
    
    remaining_json = {"energy_remaining":energy_remaining, "vitD_remaining":vitD_remaining, "vitC_remaining":vitC_remaining, "vitA_remaining":vitA_remaining, "vitE_remaining":vitE_remaining, "calcium_remaining":calcium_remaining, "iron_remaining":iron_remaining, "potassium_remaining":potassium_remaining}
    
    for key, value in remaining_json.items():
        if value <= 0:
            remaining_json[key] = 0
    #return remaining_json
    # find the largest three nutrients they are missing

    sorted_values = sorted(remaining_json.values(), reverse=True)
    largest_values = {}
    for key, value in remaining_json.items():
        if value in sorted_values[:2]:
            largest_values[key] = value

    remaining_nutrients = list(largest_values.keys()) # nutrients to add in url query

    nutrients_query = ""
    for i in range(len(list(largest_values.keys()))):

        if "energy" in remaining_nutrients[i]:
            nutrients_query += "&minCalories="+str((float(list(largest_values.values())[i]))/2-25)+"&maxCalories="+str((float(list(largest_values.values())[i]))/2+50)
        if "calcium" in remaining_nutrients[i]:
            nutrients_query += "&minCalcium="+str((float(list(largest_values.values())[i]))/2-25)+"&maxCalcium="+str((float(list(largest_values.values())[i]))/2+50)
        if "iron" in remaining_nutrients[i]:
            nutrients_query += "&minIron="+str((float(list(largest_values.values())[i]))/2-1)+"&maxIron="+str((float(list(largest_values.values())[i]))/2+3)
        if "potassium" in remaining_nutrients[i]:
            nutrients_query += "&minPotassium="+str((float(list(largest_values.values())[i]))/2-250)+"&maxPotassium="+str((float(list(largest_values.values())[i]))/2+500)
        if "vitD" in remaining_nutrients[i]:
            nutrients_query += "&minVitaminD="+str((float(list(largest_values.values())[i]))/2-5)+"&maxVitaminD="+str((float(list(largest_values.values())[i]))/2+10)
        if "vitA" in remaining_nutrients[i]:
            nutrients_query += "&minVitaminA="+str((float(list(largest_values.values())[i]))/2-50)+"&maxVitaminA="+str((float(list(largest_values.values())[i]))/2+100)
        if "vitC" in remaining_nutrients[i]:
            nutrients_query += "&minVitaminC="+str((float(list(largest_values.values())[i]))/2-10)+"&maxVitaminC="+str((float(list(largest_values.values())[i]))/2+20)
        if "vitE" in remaining_nutrients[i]:
            nutrients_query += "&minVitaminE="+str((float(list(largest_values.values())[i]))/2-2)+"&maxVitaminE="+str((float(list(largest_values.values())[i]))/2+5)
    
    # find snacks that fulfill these remaining nutrients

    find_remaining_url = "https://api.spoonacular.com/recipes/complexSearch"

    # ingredient preferences are randomized, includes will be added less than 20% of the time due to how much it limits the results
    micros_query_params = ""
    micros_query_params = "apiKey=" + api_key + nutrients_query + diet_string+excludes+"&type=snack,drink,side dish,appetizer,salad,soup,fingerfood"

    micros_query =  find_remaining_url + "?" + micros_query_params 
    micros_response = (requests.get(micros_query)).json()
    ids_list = []
    for i in range(len(micros_response["results"])):
        ids_list.append(micros_response["results"][i]["id"])

    # choose at most two - no user choice
    if len(ids_list) >2:
        ids_list = random.sample(ids_list, 2)

    ids_list_str = [str(val) for val in ids_list]

    ids_string = ','.join(ids_list_str)
    recipes_string = ','.join(recipes)

    put_string = recipes_string + "," + ids_string

    update = WeeklyRecipes.query.filter_by(week_number_ID = weekID, userID = userID)
    update.update(dict(recipeIDs = put_string))

    db.session.commit()

    # time end for function
    end_time = time.time()
    total_time = end_time - start_time

    time_taken = Latency("generate_remaining_recipes", total_time)
    db.session.add(time_taken)
    db.session.commit()

    # post grocery list:

    recipe_ids = WeeklyRecipes.query.filter_by(userID = userID, week_number_ID = weekID).one()
    recipes = (recipe_ids.recipeIDs.replace(" ", "")).split(',')
    
    num_recipes = len(recipes)
    
    recipe_ingredients_info_json = {}
    
    find_by_nutrients_url = "https://api.spoonacular.com/recipes/{id}/ingredientWidget.json?apiKey=13cc54269ca54d258cf7b07e4383154c"
    
    grocery_list_map = {}
    
    for recipe in recipes:
        add = "https://api.spoonacular.com/recipes/"+str(recipe)+"/ingredientWidget.json?apiKey=13cc54269ca54d258cf7b07e4383154c"
        add_response = requests.get(add)
        recipe_ingredients_info_json[str(recipe)] = add_response.json()
        
        for i in range(len(recipe_ingredients_info_json[recipe]["ingredients"])):
            if (str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"]) in grocery_list_map):
                
                # then add to already existing amount
                temp = float((grocery_list_map[str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"])]).split(" ")[0])
                
                add = temp + float(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["value"])*(7/num_recipes)
                
                grocery_list_map[str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"])] = str(round(add, 2))+ " " +str(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["unit"])
                
            else:
                add = float(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["value"])*(7/num_recipes)
                grocery_list_map[str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"])] = str(round(add ,2) ) + " " +str(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["unit"])
    
    #return json.dumps(grocery_list_map)
    # post information to nutrition table in db
    post_grocery_list = GroceryLists(userID, weekID, json.dumps(grocery_list_map))
  
    db.session.add(post_grocery_list)
    db.session.commit()

    return "recipe to fill nutrient requirement added and grocery list is posted"
    
@app.route('/post_grocery_list/<userID>/<weekID>', methods=['GET','POST'])
def post_grocery_list(userID, weekID):
    
    # time start for function
    # time is in seconds
    start_time = time.time()

    ###
    recipe_ids = WeeklyRecipes.query.filter_by(userID = userID, week_number_ID = weekID).one()
    recipes = (recipe_ids.recipeIDs.replace(" ", "")).split(',')
    
    num_recipes = len(recipes)
    
    recipe_ingredients_info_json = {}
    
    find_by_nutrients_url = "https://api.spoonacular.com/recipes/{id}/ingredientWidget.json?apiKey=13cc54269ca54d258cf7b07e4383154c"
    
    grocery_list_map = {}
    grocery_list_map["id"] = weekID
    
    for recipe in recipes:
        add = "https://api.spoonacular.com/recipes/"+str(recipe)+"/ingredientWidget.json?apiKey=13cc54269ca54d258cf7b07e4383154c"
        add_response = requests.get(add)
        recipe_ingredients_info_json[str(recipe)] = add_response.json()
        
        for i in range(len(recipe_ingredients_info_json[recipe]["ingredients"])):
            if (str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"]) in grocery_list_map):
                
                # then add to already existing amount
                temp = float((grocery_list_map[str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"])]).split(" ")[0])
                
                add = temp + float(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["value"])*(7/num_recipes)
                
                grocery_list_map[str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"])] = str(round(add, 2))+ " " +str(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["unit"])
                
            else:
                add = float(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["value"])*(7/num_recipes)
                grocery_list_map[str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"])] = str(round(add ,2) ) + " " +str(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["unit"])
    
    
    #return json.dumps(grocery_list_map)
    # post information to nutrition table in db
    post_grocery_list = GroceryLists(userID, weekID, json.dumps(grocery_list_map))
  
    db.session.add(post_grocery_list)
    db.session.commit()

    # time end for function
    end_time = time.time()
    total_time = end_time - start_time

    time_taken = Latency("generate_grocery_list", total_time)
    db.session.add(time_taken)
    db.session.commit()

    return "grocery list added to database" # weekly


@app.route('/get_grocery_list/<userID>/<weekID>', methods=['GET'])
def get_grocery_list(userID, weekID):
    get =  GroceryLists.query.filter_by(userID = userID, week_number_ID = weekID).one()
    get_grocery_list = get.grocery_list
    grocery_dict = json.loads(get_grocery_list)
    print(grocery_dict)
    return grocery_dict

@app.route('/get_num_weeks/<userID>', methods=['GET'])
def get_num_weeks(userID):
    get = db.session.query(WeeklyRecipes.week_number_ID).filter_by(userID = userID).count()
    return str(get)