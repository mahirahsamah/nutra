from flask import Blueprint

nutrition = Blueprint('nutrition', __name__)

@nutrition.route('/nutrition')
def home():
    return "groceriiies"