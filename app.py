#!/usr/bin/env
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# turn tracking off
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# this key SHOULD be SECRET!
app.secret_key = 'seraphina'
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth

# resource Item now accessible via API
api.add_resource(
    Item,
    '/item/<string:name>'
)
api.add_resource(
    ItemList,
    '/items'
)
api.add_resource(
    UserRegister,
    '/register'
)

api.add_resource(
    Store,
    '/store/<string:name>'
)

api.add_resource(
    StoreList,
    '/stores'
)

# how to avoid running app.py from import
if __name__ == '__main__':
    app.run(port=5000, debug=False)
