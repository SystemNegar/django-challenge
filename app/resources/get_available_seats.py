from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt
from resources.user import is_admin
from models.matches import MatchesModel
from models.stadium import StadiumModel
from models.cache_manager import get_match_seats

from ast import literal_eval
import copy


class GetAvailableSeats(Resource):

    def get(self,id):
        available_seats=[]
        match = MatchesModel.find_by_id(id)
        stadium = StadiumModel.find_by_id(match.json()[id])
        segment_dict = literal_eval(stadium.json()['segments'])

        for seg in segment_dict.keys():
            for row in segment_dict[seg]:
                ind = 2**(segment_dict[seg][row])
            seats=[]

        cache_data = get_match_seats