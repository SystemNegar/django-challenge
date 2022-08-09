from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt
from resources.user import is_admin
from models.matches import MatchesModel


_parser = reqparse.RequestParser()
_parser.add_argument('datetime',
                          type=str,
                          required=True,
                          help="datetime cannot be blank."
                          )

_parser.add_argument('capacity',
                          type=int,
                          required=True,
                          help="capacity cannot be blank."
                          )

_parser.add_argument('teams',
                          type=str,
                          required=True,
                          help="teams cannot be blank."
                          )

_parser.add_argument('stadium_id',
                          type=int,
                          required=True,
                          help="stadium_id cannot be blank."
                          )
class Matches(Resource):

    
    def get(self, name):
        if not is_admin():
            return {"message": "Not authorized for this action"}, 400 
        match = MatchesModel.find_by_name(name)
        if match:
            return match.json()
        return {'message': 'match not found'}, 404
        

    def post(self, name):
        if not is_admin():
            return {"message": "Not authorized for this action"}, 400 
        if MatchesModel.find_by_name(name):
            return {'message': "An match with name '{}' already exists.".format(name)}, 400

        data = _parser.parse_args()

        match = MatchesModel(name, **data)

        try:
            match.save_to_db()
        except:
            return {"message": "An error occurred inserting the match."}, 500

        return match.json(), 201

    def delete(self, name):
        if not is_admin():
            return {"message": "Not authorized for this action"}, 400 
        claims = get_jwt()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        match = MatchesModel.find_by_name(name)
        if match:
            match.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        if not is_admin():
            return {"message": "Not authorized for this action"}, 400 
        data = _parser.parse_args()
        match = MatchesModel(name, **data)
        match.save_to_db()
        return match.json()


class MatchesList(Resource):
    def get(self):
        if not is_admin():
            return {"message": "Not authorized for this action"}, 400 
        
        return [match.json() for match in MatchesModel.find_all()]

