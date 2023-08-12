#!/usr/bin/env python3

from models import db, Swimmer, Team, Event, Time
from flask_migrate import Migrate
from flask import Flask, request, make_response
from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

@app.route('/')
def index():
    return '<h1>Is this thing on?</h1>'

class Events(Resource):

    def get(self):
        return make_response([e.to_dict(rules=("-times", "-swimmer", )) for e in Event.query.all()])

api.add_resource(Events, "/events")


if __name__ == '__main__':
    app.run(port=5555, debug=True)
