import string
from flask_restful import Resource,reqparse
from models.stadium import StadiumModel
from resources.user import is_admin


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


class Stadium(Resource):

    def get(self, name):
        if is_admin():
            stadium = StadiumModel.find_by_name(name)
            if stadium:
                return stadium.json()
            return {'message': 'stadium not found'}, 401
        return {"message": "Not authorized for this action"}, 400

    def post(self, name):
        if is_admin():
            if StadiumModel.find_by_name(name):
                return {'message': "A stadium with name '{}' already exists.".format(name)}, 400

            data = _parser.parse_args()
            stadium = StadiumModel(name, **data)
            try:
                stadium.save_to_db()
            except:
                return {"message": "An error occurred creating the stadium."}, 500

            return stadium.json(), 201
        return {"message": "Not authorized for this action"}, 400

    def delete(self, name):
        if is_admin():
            stadium = StadiumModel.find_by_name(name)
            if stadium:
                stadium.delete_from_db()

            return {'message': 'stadium deleted'}
        return {"message": "Not authorized for this action"}, 400

class StadiumList(Resource):    
    def get(self):
        if is_admin():
            return {'stadium': [x.json() for x in StadiumModel.find_all()]}
        return {"message": "Not authorized for this action"}, 400   
