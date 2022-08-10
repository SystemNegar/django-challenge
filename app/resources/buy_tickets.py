"""
for reserve seat, we change all row of seats to binary numbers, for example if 
length of one row is 4 related row number becomes 0b10000, and save this on redis
for check a seat we and it to related place of seat in row if result becomes zero 
it means the seat is available and for reserve it we convert this bit from 0 to 1
then save the related data in sql database
"""
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.matches import MatchesModel
from models.get_account_balance import is_balance_sufficient
from models.seat_manager import register_ticket, is_seat_available
from models.reserved_seats import ReserveModel

from resources.matches import get_match_string
from resources.user import get_user_identity
from exceptions import MatchIdError, SeatNotAvailable, BalanceError, SaveCacheServerError

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


def intial_data_for_save_on_db(data: dict):
    return {
            'segments': data['segment'],
            'row': data['row'],
            'seat': data['seat'],
            'matches_id': data['match_id'],
            'user_id': get_user_identity()
        }

def save_data_on_db(data: dict):
    buy_data = intial_data_for_save_on_db(data)
    reserve = ReserveModel(**buy_data)
    reserve.save_to_db()
    return reserve.json()['id']

def check_and_get_match_id(match_id: int):
    match = MatchesModel.find_by_id(match_id)
    if not match:
        raise MatchIdError
    return match

class BuyTickets(Resource):
    
    def check_seat_is_available(self):
        if not is_seat_available(self.match_name_key,segment=self.data['segment'],\
                row=self.data['row'], seat_num=self.data['seat']):
            raise SeatNotAvailable

    def check_balance(self):
        if not is_balance_sufficient():
            raise BalanceError
            
    def reserve_seat_in_cache_server(self):
        if not register_ticket(self.match_name_key,segment=self.data['segment'],\
                row=self.data['row'], seat_num=self.data['seat']):
            raise SaveCacheServerError
                           
    def control_guards(self):
        self.check_seat_is_available()# guard for check seat is reserved or not
        self.check_balance()
        self.reserve_seat_in_cache_server()

    @jwt_required()
    def post(self):
        try:
            self.data = _parser.parse_args()

            match=check_and_get_match_id(self.data['match_id'])# guard for match id error
            self.match_name_key=get_match_string(match.json()['name'],match.json()['datetime'])

            self.control_guards()
            
            id = save_data_on_db(self.data)

            return {"message": f"successfull operation. your reserve id is : {id}"}

        except MatchIdError:
            return {"message":"this match id is not correct"}

        except SeatNotAvailable:
            return {"message":"this seat is not available"}

        except BalanceError:
            return {"message":"your balance is not sufficient"}

        except SaveCacheServerError:
            return {"message":"could not buy this seat"}
        

