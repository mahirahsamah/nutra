from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship 
import json
from flask_cors import CORS
import requests
import string
import os
import pprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passwd@localhost/capstone'
db = SQLAlchemy(app)
CORS(app)

# spoonacular api
#spoonacular_api_key = os.environ["SPOONACULAR_API_KEY"]
api_key = "13cc54269ca54d258cf7b07e4383154c"

class User(db.Model):

    __tablename__ = 'users_table'
    __table_args__ = {'schema': 'public'}
    
    nutrition = relationship("UserNutrition")

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

    week_number_ID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('public.users_table.userID'))
    recipeIDs = db.Column(db.String) # this is a string of comma-separated recipe IDs

    def __repr__(self):
        return f"User: {self.userID}"
    
    def __init__(self, userID, recipeIDs):
        self.userID = userID
        self.recipeIDs = recipeIDs

@app.route('/groceries')
def home():
    return "Test Page"

@app.route('/post_recipes/<userID>/recipe_string', methods=['POST'])
def post_recipes(userID, recipe_string):
    #recipeID = request.json['recipeID']
    recipes = WeeklyRecipes(userID, recipe_string)

    db.session.add(recipes)
    db.session.commit()
    return "recipe added"

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
    "gender": "female",
    "weight_lbs" : 126,
    "age" : 30,
    "height_feet" :5,
    "height_inches" :5,
    "activity_level":"low",
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
    
    nutrients_response = requests.get(f'http://localhost:5000/get_nutrition/{userID}')
    nutrients_amounts = nutrients_response.json()
    
    #return nutrients_amounts
    #return nutrients_amounts
    #data = json.loads(nutrients_amounts)

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
    
    find_by_nutrients_url = "https://api.spoonacular.com/recipes/findByNutrients"

    # divide nutrients by 2 to account for lunch and dinner meals
    macros_query_params = "apiKey=" + api_key + "&minProtein="+str(float(protein)/2-20)+"&maxProtein="+str(float(protein)/2+20)+"&minFat="+str(float(fat)/2-20)+"&maxFat="+str(float(fat)/2+20)+"&minCarbs="+str(float(carbs)/2-20)+"&maxCarbs="+str(float(carbs)/2+20)#+"&minVitaminD="+str(float(vitD)/2-2)+"&maxVitaminD="+str((float(vitD)+float(vitD_ul))/4)#+"&minVitaminC="+str(float(vitC)-20)+"&maxVitaminC="+str((float(vitC)+float(vitC_ul))/2)+"&minVitaminA="+str(float(vitA)-20)+"&maxVitaminA="+str((float(vitA)+float(vitA_ul))/2)+"&minVitaminE="+str(float(vitE)-20)+"&maxVitaminE="+str((float(vitE)+float(vitE_ul))/2)+"&minCalcium="+str(float(calcium)-20)+"&maxCalcium="+str((float(calcium)+float(calcium_ul))/2)+"&minIron="+str(float(iron)-20)+"&maxIron="+str((float(iron)+float(iron_ul))/2)+"&minPotassium="+str(float(potassium)-20)+"&maxPotassium="+str(float(potassium)+20)+"&number=10"
    
    # having the micronutrients in the query params makes it more constricting. so i am just going to let the user choose from list of recipes and then fill the rest of the nutrients in with snacks

    macros_query =  find_by_nutrients_url + "?" + macros_query_params 
    
    macros_response = requests.get(macros_query)
    return macros_response.json()

# NOT DONE 

@app.route('/get_remaining_ingredients/<userID>', methods=['GET'])
def get_remaining_ingredients(userID):

    # get recipes IDs from the weekly recipes table
    recipe_ids = WeeklyRecipes.query.filter_by(userID = userID).one()
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
    vitD_ul = str(micronutrients.vitD_ul)
    vitC_ul = str(micronutrients.vitC_ul)
    vitA_ul = str(micronutrients.vitA_ul)
    vitE_ul = str(micronutrients.vitE_ul)
    calcium_ul = str(micronutrients.calcium_ul)
    iron_ul = str(micronutrients.iron_ul)

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
        
        energy_sum += int(recipe_nutrition_info_json[str(recipe)]["bad"][0]["amount"])

        for i in range(len(recipe_nutrition_info_json[str(recipe)]["good"])):
        
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Calcium":
                calcium_sum += int(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin C":
                vitC_sum += int(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin A":
                vitA_sum += int(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin E":
                vitE_sum += int(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin D":
                vitD_sum += int(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin D":
                iron_sum += int(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
            if recipe_nutrition_info_json[str(recipe)]["good"][i]["title"] == "Vitamin D":
                potassium_sum += int(recipe_nutrition_info_json[str(recipe)]["good"][i]["amount"][:-2])
        
    # remaining nutrients
    energy_remaining = float(energy) - float(energy_sum)

    vitD_remaining = float(vitD) - float(vitD_sum)
    vitC_remaining = float(vitC) - float(vitC_sum)
    vitA_remaining = float(vitA) - float(vitA_sum)
    vitE_remaining = float(vitE) - float(vitE_sum)
    calcium_remaining = float(calcium) - float(calcium_sum)
    iron_remaining = float(iron) - float(iron_sum)
    potassium_remaining = float(potassium) - float(potassium_sum)
    
    remaining_json = {"energy_remaining":energy_remaining, "vitD_remaining":vitD_remaining, "vitC_remaining":vitC_remaining, "vitA_remaining":vitA_remaining, "vitE_remaining":vitE_remaining, "calcium_remaining":calcium_remaining, "iron_remaining":iron_remaining, "potassium_remaining":potassium_remaining}
    
    for key, value in remaining_json.items():
        if value <= 0:
            remaining_json[key] = 0
            
            
    # find snacks that fulfill these remaining nutrients
    '''
    find_grocery_products = "https://api.spoonacular.com/food/products/search" # packaged foods
    find_ingredients = "https://api.spoonacular.com/food/ingredients/search" # whole foods

    # divide nutrients by 2 to account for lunch and dinner meals
    grocery_query_params = "apiKey=" + api_key + "&number=5"
    grocery_query =  find_grocery_products + "?" + grocery_query_params 
    
    grocery_response = (requests.get(grocery_query)).json()
    '''
    return remaining_json

# https://api.spoonacular.com/food/products/search?apiKey=13cc54269ca54d258cf7b07e4383154c&query=pizza&number=5

@app.route('/get_grocery_list/<userID>', methods=['GET'])
def get_grocery_list(userID):
    
    recipe_ids = WeeklyRecipes.query.filter_by(userID = userID).one()
    recipes = (recipe_ids.recipeIDs.replace(" ", "")).split(',')
    
    recipe_ingredients_info_json = {}
    
    find_by_nutrients_url = "https://api.spoonacular.com/recipes/{id}/ingredientWidget.json?apiKey=13cc54269ca54d258cf7b07e4383154c"
    
    grocery_list_map = {}
    
    for recipe in recipes:
        add = "https://api.spoonacular.com/recipes/"+str(recipe)+"/ingredientWidget.json?apiKey=13cc54269ca54d258cf7b07e4383154c"
        add_response = requests.get(add)
        recipe_ingredients_info_json[str(recipe)] = add_response.json()
        
        for i in range(len(recipe_ingredients_info_json[recipe]["ingredients"])):
            #print(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"])
            if (str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"]) in grocery_list_map):
                
                # then add to already existing amount
                temp = float((grocery_list_map[str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"])]).split(" ")[0])
                #return str(temp)
                
                #temp2 = temp.maketrans('','') 
                
                #nodigs=temp2.translate(temp2, string.digits)
                #temp.translate(temp2, nodigs)
                
                #temp = float(temp)
                
                add = temp + float(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["value"])*7
                
                grocery_list_map[str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"])] = add+ " " +str(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["unit"])
                
            else:
                grocery_list_map[str(recipe_ingredients_info_json[recipe]["ingredients"][i]["name"])] = str(float(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["value"])*7) + " " +str(recipe_ingredients_info_json[recipe]["ingredients"][i]["amount"]["us"]["unit"])
        
    return grocery_list_map # weekly
