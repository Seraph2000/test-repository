import sqlite3
from db import db


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # not using self here, so we can make this a @classmethod!
    @classmethod
    def find_by_username(cls, username):
        # col name = arg name
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return UserModel.query.filter_by(id=_id).first()