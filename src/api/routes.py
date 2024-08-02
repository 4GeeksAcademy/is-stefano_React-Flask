"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Users, Posts, Comments, Followers, Medias
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/users', methods=['GET', 'POST'])
def handle_users():
    response_body = {}
    if request.method == 'GET':
        rows = db.session.execute(db.select(Users)).scalars()
        results = [row.serialize() for row in rows]  # List comprehension
        response_body['results'] = results
        response_body['message'] = "GET received"
        return response_body, 200
    
    if request.method == 'POST':
        data = request.json
        username = data.get('username', None)
        email = data.get('email', None)
        if not username or not email:
            response_body['message'] = 'Missing data'
            response_body['results'] = {}
            return response_body, 400
        
        username_exist = db.session.execute(db.select(Users).where(Users.username == username)).scalar()
        email_exist = db.session.execute(db.select(Users).where(Users.email == email)).scalar()
        if username_exist or email_exist:
            response_body['message'] = 'User already exist'
            response_body['results'] = {}
            return response_body, 404
        row = Users(username = data['username'], 
                    email = data['email'],
                    firstname = data['firstname'],
                    lastname = data['lastname'])
        db.session.add(row)
        db.session.commit()
        response_body['message'] = "POST received"
        return response_body, 200


@api.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    response_body = {}
    if request.method == 'GET':
        row = db.session.execute(db.select(Users).where(Users.id == user_id)).scalar()
        if not row:
            response_body['results'] = {}
            response_body['message'] = f'User doesnt exist {user_id}'
            return response_body, 404
        response_body['results'] = row.serialize()
        response_body['message'] = f'GET received {user_id}'
        return response_body, 200
    
    if request.method == 'PUT':
        data = request.json
        username = data.get('username', None)
        email = data.get('email', None)
        if not username or not email:
            response_body['message'] = 'Missing data'
            response_body['results'] = {}
            return response_body, 400
        
        user = db.session.execute(db.select(Users).where(Users.id == user_id)).scalar()
        if not user:
            response_body['message'] = f'User doesnt exist {user_id}'
            response_body['results'] = {}
            return response_body, 404
        
        username_exist = db.session.execute(db.select(Users).where(Users.username == username, Users.id != user_id)).scalar()
        email_exist = db.session.execute(db.select(Users).where(Users.email == email, Users.id != user_id)).scalar()
        if username_exist or email_exist:
            response_body['message'] = 'User already exist'
            response_body['results'] = {}
            return response_body, 409
        user.username = username
        user.email = email
        user.firstname = data.get('firstname', user.firstname)
        user.lastname = data.get('lastname', user.lastname)
        db.session.commit()
        response_body['message'] = "User updated successfully"
        response_body['results'] = user.serialize()
        return response_body, 200
    
    if request.method == 'DELETE':
        user = db.session.execute(db.select(Users).where(Users.id == user_id)).scalar()
    if not user:
        response_body['message'] = f'User doesnt exist {user_id}'
        response_body['results'] = {}
        return response_body, 404
    
    db.session.delete(user)
    db.session.commit()
    response_body['message'] = f'User {user_id} deleted successfully'
    return response_body, 200

def handle_followers():
    response_body = {}
    if request.method == 'GET':
        rows = db.session.execute(db.select(Followers)).scalars()
        results = [row.serialize() for row in rows]
        response_body['results'] = results
        response_body['message'] = "recibí el GET request"
        return response_body, 200
    
    if request.method == 'POST':
        data = request.json
        following = data.get("following", None)
        follower = data.get("follower", None)
        print(data)
        if not follower or not following:
            response_body['message'] = 'Faltan datos'
            response_body['results'] = {}
            return response_body, 404
        
        if not (isinstance(follower, int) and isinstance(following, int)):
            response_body['message'] = 'Los datos deben ser números'
            response_body['results'] = {}
            return response_body, 404

        following_exist = db.session.get(Followers, following)
        follower_exist = db.session.get(Followers, follower)
        if not follower_exist or not following_exist or following == follower:
            response_body['message'] = 'Algono o Ambos usuarios no existen o son iguales'
            response_body['results'] = {}
            return response_body, 404
        row = Followers(user_from_id = data['following'], 
                        user_to_id = data['follower'])
        db.session.add(row)
        db.session.commit()
        response_body['message'] = "recibí el POST request"
        return response_body, 200


@api.route("/login", methods=["POST"])
def login():
    response_body = {}
    data = request.json
    username = data.get("username", None)
    password = data.get("password", None)
    # TODO: realizar la logica para verificar en nuestra DB
    if username != "test" or password != "test":
        response_body['message'] = "Bad username or password"
        return response_body, 401
    access_token = create_access_token(identity={'username': username, 'user_id': 30, 'is_admin': True})
    response_body['message'] = 'User logged'
    response_body['access token'] = access_token
    # return jsonify(access_token=access_token)
    return response_body, 200

@api.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    response_body = {}
    current_user = get_jwt_identity()
    # return jsonify(logged_in_as=current_user), 200
    response_body['message'] = f'Acceso concedido a {current_user}'
    return response_body, 200

@api.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    response_body = {}
    current_user = get_jwt_identity()
    if current_user['is_admin'] == 30:
        response_body['message'] = f'Acceso concedido a {current_user["username"]}'
        response_body['user_data'] = current_user
        return response_body, 200
    response_body['message'] = f'Acceso denegado, no eres el usuario 30'
    response_body['user_data'] = {current_user}
    return response_body, 403
