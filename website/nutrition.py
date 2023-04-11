from flask import Blueprint, render_template

nutrition = Blueprint('nutrition', __name__)

@nutrition.route('/groceries')
def home():
    return render_template("groceries.html")

# stopped at 42:52