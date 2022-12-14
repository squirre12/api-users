from flask_restful import Resource
from starlette import status

from src import db
from flask import request
from ..models import User
import bcrypt


class Users(Resource):
    @staticmethod
    def get(idx=None):
        if not idx:
            users = db.session.query(User).all()
            data = [user.to_dict() for user in users]
            return data, status.HTTP_200_OK
        user = db.session.query(User).filter_by(id=idx).first()
        if not user:
            return status.HTTP_204_NO_CONTENT
        return user.to_dict(), status.HTTP_200_OK

    @staticmethod
    def post():
        user_json = request.json
        if not user_json:
            return "Wrong data", status.HTTP_204_NO_CONTENT
        try:
            user = User(
                username=user_json["username"],
                email=user_json["email"],
                password=bcrypt.hashpw(
                    user_json["password"].encode(), bcrypt.gensalt()
                ),
            )
            db.session.add(user)
            db.session.commit()
        except (ValueError, KeyError):
            return "Wrong data", status.HTTP_400_BAD_REQUEST
        return "Create successfully", status.HTTP_201_CREATED

    @staticmethod
    def put(idx):
        user_json = request.json
        if not user_json:
            return "User doesn't exist", status.HTTP_204_NO_CONTENT
        try:
            db.session.query(User).filter_by(id=idx).update(
                dict(
                    username=user_json["username"],
                    email=user_json["email"],
                    password=bcrypt.hashpw(
                        user_json["password"].encode(), bcrypt.gensalt()
                    ),
                )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return "Wrong data", status.HTTP_204_NO_CONTENT
        return "Create successfully", status.HTTP_201_CREATED

    @staticmethod
    def patch(idx):
        user = db.session.query(User).filter_by(id=idx).first()
        if not user:
            return "User doesn't exist", status.HTTP_204_NO_CONTENT
        user_json = request.json
        username = user_json.get("username")
        email = user_json.get("email")
        password = user_json.get("password")
        if username:
            user.username = username
        elif email:
            user.email = email
        elif password:
            user.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        db.session.add(user)
        db.session.commit()
        return "Create successfully", status.HTTP_201_CREATED

    @staticmethod
    def delete(idx):
        user = db.session.query(User).filter_by(id=idx).first()
        if not user:
            return "User doesn't exist", status.HTTP_204_NO_CONTENT
        db.session.delete(user)
        db.session.commit()
        return "Update successfully", status.HTTP_202_ACCEPTED
