from flask import Flask
from flask_peewee.db import Database

app = Flask(__name__)

app.config.from_object('testflaskapp.config')

db = Database(app)

@app.route('/')
def index():
    return "This is just a test app. It doesn't do much."

if __name__ == '__main__':
    app.run()
