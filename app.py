from flask import Flask, render_template, request
#from sqlalchemy import SQLAlchemy

app = Flask(__name__)
#db = SQLAlchemy(app)

@app.route('/')
def index ():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)