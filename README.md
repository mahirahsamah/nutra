## Setting up the database

In the backend folder, type:

python

from app import app, db

app.app_context().push()

db.create_all()

## Running REST

Start backend server with: python -m flask run
 
Start frontend server with: npm start

Both servers should have the same localhost port.

