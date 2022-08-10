from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import jwt_required, get_jwt,get_jwt_identity
from models.user import UserModel


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

class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201

class AdminUserRegister(Resource):
    def post(self):
        if is_admin():
            data = _user_parser.parse_args()
            data['role'] = "admin"
            if UserModel.find_by_username(data['username']):
                return {"message": "A user with that username already exists"}, 400

            user = UserModel(**data)
            user.save_to_db()

            return {"message": "Admin created successfully."}, 201
        return {"message": "Not authorized for this action"}, 400


class User(Resource):

    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        return user.json(), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200


class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()

        user = UserModel.find_by_username(data['username'])

        if user and check_password_hash(user.password, data['password']):
            additional_claims = {"role": user.role}
            access_token = create_access_token(identity=user.id, additional_claims=additional_claims, fresh=True) 
            refresh_token = create_refresh_token(user.id)
            return {'access_token': access_token}, 200

        return {"message": "Invalid Credentials!"}, 401
