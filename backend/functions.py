def nutrients_amounts(gender, weight_lbs, age, height_feet, height_inches, activity_level, strength_training):
    # returns an array in the format: [kcals, protein, fat, carbs, ...]
    
    # protein
    # fats
    # carbohydrates
    # vitamins
    # minerals

    weight_kg = weight_lbs/2.20462262185
    height_cm = (height_feet + height_inches/12) * 30.48
    
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
    
    return [energy, protein, fat, carbs]
    
