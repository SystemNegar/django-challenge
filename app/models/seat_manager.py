from models.cache_manager import get_match_seats,set_match_seat
from exceptions import SeatNumberError

def check_is_seat_num_valid(seat_num: int, length: int):
    if  seat_num > length:
        raise SeatNumberError
        

def get_seats_and_prepare_for_binary(match: str, segment: str,row: str):
    segment=get_match_seats(match, segment)    
    row_array=int(bin(segment[row]), base=2)
    return segment, row_array, len(bin(segment[row])) -3

def is_seat_available(match: str, segment: str, row: str, seat_num: int) -> bool:
    s, row_array, length= get_seats_and_prepare_for_binary(match,segment,row) 
    if (row_array & int(bin(2**length),base=2)>>(seat_num) == 0):
        return True
    return False

def register_ticket(match: str, segment: str, row: str, seat_num) -> bool:
    try:
        seg, row_array, length= get_seats_and_prepare_for_binary(match, segment, row)
        check_is_seat_num_valid(seat_num, length)# guard for seat number error

        seg[row] = row_array | int(bin(2**length), base=2)>>seat_num

        if set_match_seat(match, segment, **seg) is not None:
            return True
        return False

    except SeatNumberError:
        return {"message" : "seat number is not correct"}

    except Exception as e:
        return {"message" : f"Exception {e}"}
