#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Game/Review/User API"


@app.route("/game")
def game():
   
    games=[]
    for game in Game.query.all():
        game_dict={
            "title":game.title,
            "genre":game.genre,
            "platform":game.platform,
            "price":game.price,

        }
        games.append(game_dict)
    response =make_response(
        jsonify(games),
        200)
    response.headers["Content-Type"] ="application/json"

    return response    

@app.route("/game/<int:id>")
def sport(id):

    sport =Game.query.filter(Game.id==id).first()
    game_dict=sport.to_dict()

    response=make_response(jsonify(game_dict),200)
    response.headers["Content-Type"]="application/json"

    return response    



if __name__ == '__main__':
    app.run(port=5555, debug=True)