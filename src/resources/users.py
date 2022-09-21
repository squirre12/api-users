from flask_restful import Resource
from src import db
from flask import request
from ..models import User
import bcrypt

class Users(Resource):

    def get(self, id=None):
        if not id:
            users = db.session.query(User).all()
            return [user.to_dict() for user in users], 200
        user = db.session.query(User).filter_by(id=id).first()
        if not user:
            return '', 404
        return user.to_dict(), 200

    def post(self):
        user_json = request.json
        if not user_json:
            return {'message': 'wrong data'}, 400
        try:
            user = User(
                username=user_json['username'],
                email=user_json['email'],
                password=bcrypt.hashpw(user_json['password'].encode(), bcrypt.gensalt())
            )
            db.session.add(user)
            db.session.commit()
        except(ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': "Created successfully"}, 201

    def put(self, id):
        user_json = request.json
        if not user_json:
            return {'message': 'wrong data'}, 400
        try:
            db.session.query(User).filter_by(id=id).update(
                dict(
                    username=user_json['username'],
                    email=user_json['email'],
                    password=bcrypt.hashpw(user_json['password'].encode(), bcrypt.gensalt())
                )
            )
            db.session.commit
        except(ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': "Created successfully"}, 201

    def patch(self, id):
        user = db.session.query(User).filter_by(id=id).first()
        if not user:
            return {'message': 'wrong data'}, 400
        user_json = request.json
        username = user_json.get('username')
        email = user_json.get('email')
        password = user_json.get('password')
        if username:
            user.username = username
        elif email:
            user.email = email
        elif password:
            user.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        db.session.add(user)
        db.session.commit()
        return {'message': "Update successfully"}, 201

    def delete(self, id):
        user = db.session.query(User).filter_by(id=id).first()
        if not user:
            return {'message': 'wrong data'}, 400
        db.session.delete(user)
        db.session.commit()
        return {'message': 'Deleted successfully'}, 202