from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db
from resources.user import UserRegister, User, UserLogin,AdminUserRegister
from resources.matches import Matches, MatchesList
from resources.stadium import Stadium, StadiumList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jsoisnea1259865774364fgh'  
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)


api.add_resource(Stadium, '/stadium/<string:name>')
api.add_resource(StadiumList, '/stadium')
api.add_resource(Matches, '/match/<string:name>')
api.add_resource(MatchesList, '/matches')
api.add_resource(UserRegister, '/register')
api.add_resource(AdminUserRegister, '/adminregister')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
