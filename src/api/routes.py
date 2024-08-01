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
