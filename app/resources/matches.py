from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt

from resources.user import check_user_is_admin

from models.matches import MatchesModel
from models.stadium import StadiumModel
from models.cache_manager import set_match_seat

from exceptions import MatchNameError

from ast import literal_eval
import copy


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

def get_match_string(name,datetime):
    return f"{name}-{datetime}"

def check_exist_and_get_match_by_name(name,message=None):
    match = MatchesModel.find_by_name(name)
    if not match:
        raise MatchNameError(message)
    return match

def check_not_exist_and_get_match_by_name(name,message=None):
    match = MatchesModel.find_by_name(name)
    if match:
        raise MatchNameError(message)
    return match


class Matches(Resource):

    def convert_row_cap_to_int_and_cache(self, name: str, stadium_id: int, data: dict):
        stadium = StadiumModel.find_by_id(stadium_id)
        segment_dict = literal_eval(stadium.json()['segments'])
        change_dict = copy.deepcopy(segment_dict)

        for seg in segment_dict.keys():
            for row in segment_dict[seg]:
                change_dict[seg][row] = 2**(segment_dict[seg][row])
            set_match_seat(name=get_match_string(name,data['datetime']),segment=seg,**change_dict[seg])
    
    def get(self, name):
        try:
            check_user_is_admin()
            match=check_exist_and_get_match_by_name(name)                
            return match.json()

        except PermissionError:
            return {"message": "Not authorized for this action"}, 400 
        
        except MatchNameError as e:
            return {'message': 'match name not found'}, 404
        

    def post(self, name):
        try:
            check_user_is_admin() 
            match=check_not_exist_and_get_match_by_name(name)                
            data = _parser.parse_args()

            match = MatchesModel(name, **data)           
            match.save_to_db()
            self.convert_row_cap_to_int_and_cache(name,data['stadium_id'],data)
            return match.json(), 201

        except PermissionError:
            return {"message": "Not authorized for this action"}, 400

        except MatchNameError:
            return {'message': "An match with name '{}' already exists.".format(name)}, 400

        except Exception as e:
            return {"message": f"Exception {e}"}, 400       

    def delete(self, name):
        try:
            check_user_is_admin() 
            match=check_exist_and_get_match_by_name(name)  
            match.delete_from_db()

        except PermissionError:
            return {"message": "Not authorized for this action"}, 400

        except MatchNameError:
            return {'message': "match name not found"}, 400

        except Exception as e:
            return {"message": f"Exception {e}"}, 400

    def put(self, name):
        try:            
            check_user_is_admin() 
            data = _parser.parse_args()
            match = MatchesModel(name, **data)
            match.save_to_db()
            return match.json()

        except PermissionError:
            return {"message": "Not authorized for this action"}, 400

        except Exception as e:
            return {"message": f"Exception {e}"}, 400


class MatchesList(Resource):

    def get(self):
        try:
            check_user_is_admin()            
            return [match.json() for match in MatchesModel.find_all()]
        except PermissionError:
            return {"message": "Not authorized for this action"}, 400

