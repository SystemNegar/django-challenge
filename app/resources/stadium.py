from flask_restful import Resource,reqparse
from models.stadium import StadiumModel
from resources.user import check_user_is_admin

from exceptions import StadiumNotExistError,StadiumExistError


_parser = reqparse.RequestParser()

_parser.add_argument('city',
                    type=str,
                    required=True,
                    help="city cannot be left blank!"
                    )
_parser.add_argument('address',
                    type=str,
                    required=True,
                    help="address cannot be left blank!"
                    )
_parser.add_argument('capacity',
                    type=int,
                    required=True,
                    help="capacity cannot be left blank!"
                    )
_parser.add_argument('number_of_segments',
                    type=int,
                    required=True,
                    help="number_of_segments cannot be left blank!"
                    )
_parser.add_argument('segments',
                    type=str,
                    required=True,
                    help="segments cannot be left blank!"
                    )

def check_exist_and_get_stadium_by_name(name):
    stadium = StadiumModel.find_by_name(name)
    if not stadium:
        raise StadiumNotExistError
    return stadium

def check_not_exist_and_get_stadium_by_name(name):
    stadium = StadiumModel.find_by_name(name)
    if stadium: 
        raise StadiumExistError       
    return stadium
    

class Stadium(Resource):

    def get(self, name):
        try:
            check_user_is_admin()
            stadium = check_exist_and_get_stadium_by_name(name)
            return stadium.json()   

        except PermissionError:
            return {"message": "Not authorized for this action"}, 400 
        except StadiumNotExistError:
            return {'message': 'stadium not found'}, 400 

    def post(self, name):
        try:
            check_user_is_admin()
            check_not_exist_and_get_stadium_by_name(name)
                
            data = _parser.parse_args()
            stadium = StadiumModel(name, **data)
            stadium.save_to_db()
            return stadium.json(), 201

        except StadiumExistError:
            return {'message': "A stadium with name '{}' already exists.".format(name)}, 400             
        except PermissionError:
            return {"message": "Not authorized for this action"}, 400
        except Exception as e:
            return {"message": f"Exception {e}"}, 400

    def delete(self, name):
        try:
            check_user_is_admin()
            stadium = check_exist_and_get_stadium_by_name(name)
            stadium.delete_from_db()
            return {'message': 'stadium deleted'}

        except PermissionError:
            return {"message": "Not authorized for this action"}, 400 
        except StadiumNotExistError:
            return {'message': 'stadium not found'}, 400 
        except:
            return {"message": "An error occurred creating the stadium."}, 400


class StadiumList(Resource):    
    def get(self):
        try:
            check_user_is_admin()
            return {'stadium': [x.json() for x in StadiumModel.find_all()]}
        except PermissionError:
            return {"message": "Not authorized for this action"}, 400    
