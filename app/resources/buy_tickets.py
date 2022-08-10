from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from resources.matches import get_match_string
from models.matches import MatchesModel
from models.get_account_balance import is_balance_sufficient
from models.seat_manager import register_ticket,is_seat_available

_parser = reqparse.RequestParser()

_parser.add_argument('match_id',
                    type=int,
                    required=True,
                    help="match_id cannot be left blank!"
                    )
_parser.add_argument('segment',
                    type=str,
                    required=True,
                    help="segment cannot be left blank!"
                    )
_parser.add_argument('row',
                    type=str,
                    required=True,
                    help="row cannot be left blank!"
                    )
_parser.add_argument('seat',
                    type=int,
                    required=True,
                    help="seat cannot be left blank!"
                    )



class BuyTickets(Resource):

    @jwt_required()
    def post(self):
        data = _parser.parse_args()
        match = MatchesModel.find_by_id(data['match_id'])#**
        match_name_key=get_match_string(match.json()['name'],match.json()['datetime'])
        if not is_seat_available(match_name_key,segment=data['segment'], row=data['row'], seat_num=data['seat']):
            return {"message":"this seat is not available"}

        if not is_balance_sufficient():
            return {"message":"your balance is not sufficient"}

        if not register_ticket(match_name_key,segment=data['segment'], row=data['row'], seat_num=data['seat']):
            return {"message":"could not buy this seat"}
        return {"message": "successfull operation"}
        

