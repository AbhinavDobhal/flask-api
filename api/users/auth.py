from os import access
from constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from flask import Blueprint, app, request, jsonify
from db.user import User
from db.database import db

auth = Blueprint("auth", __name__, url_prefix="/api/v1")


@auth.post('/register')
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    user = User(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': "User Created",
        'user': {
            'name': username, "email": email
        }
    }), HTTP_201_CREATED


@auth.get('/login')
def login():
    return {'test': 'TTTTTTT'}
