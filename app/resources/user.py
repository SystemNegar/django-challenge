from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import jwt_required, get_jwt,get_jwt_identity

from models.user import UserModel
from exceptions import UsernameError

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )


@jwt_required()
def is_admin():
    claims = get_jwt()
    if claims['role']== "admin":
        return True    
    return False

def get_user_identity():
    return get_jwt_identity()

def check_user_is_admin():
    if not is_admin():
        raise PermissionError

def check_username_not_exist(name):
    if UserModel.find_by_username(name):
        raise UsernameError

def check_exist_and_get_username_by_id(id):
    user = UserModel.find_by_id(id)
    if not user:
        raise UsernameError            
    return user

def check_exist_and_get_username_by_name(name):
        user = UserModel.find_by_username(name)
        if not user:
            raise UsernameError            
        return user

         

class UserRegister(Resource):
    def post(self):
        try:
            data = _user_parser.parse_args()

            check_username_not_exist(data['username'])
            user = UserModel(**data)
            user.save_to_db()
            return {"message": "User created successfully."}, 201

        except UsernameError:
            return {"message": "A user with that username already exists"}, 400


class AdminUserRegister(Resource):# just admin user can create another admin user
    def post(self):
        try:
            if is_admin():
                data = _user_parser.parse_args()
                data['role'] = "admin"

                check_username_not_exist(data['username'])

                user = UserModel(**data)
                user.save_to_db()
                return {"message": "Admin created successfully."}, 201
            return {"message": "Not authorized for this action"}, 400
        except UsernameError:
            return {"message": "A user with that username already exists"}, 400


class User(Resource):

    @classmethod
    def get(cls, user_id: int):
        try:
            user = check_exist_and_get_username_by_id(user_id)
            return user.json(), 200

        except UsernameError:
            return {"message": "User id not found"}, 400

    @classmethod
    def delete(cls, user_id: int):
        try:
            user = check_exist_and_get_username_by_id(user_id)
            user.delete_from_db()
            return {'message': 'User deleted.'}, 200
        except UsernameError:
            return {"message": "User id not found"}, 400


class UserLogin(Resource):
    def post(self):
        try:
            data = _user_parser.parse_args()
            user = check_exist_and_get_username_by_name(data['username'])

            if user and check_password_hash(user.password, data['password']):
                additional_claims = {"role": user.role}
                access_token = create_access_token(identity=user.id, additional_claims=additional_claims, fresh=True) 
                return {'access_token': access_token}, 200

            return {"message": "Invalid Credentials!"}, 401
            
        except UsernameError:
            return {"message": "Username not found"}, 400
