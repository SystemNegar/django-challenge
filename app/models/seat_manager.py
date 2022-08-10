from models.cache_manager import get_match_seats,set_match_seat

def get_seats_and_prepare_for_binary(match,segment,row):
    segment=get_match_seats(match,segment)
    
    row_array=int(bin(segment[row]),base=2)
    print(row_array)
    return segment, row_array, len(bin(segment[row]))-3

def is_seat_available(match,segment,row,seat_num):
    s, row_array, length= get_seats_and_prepare_for_binary(match,segment,row) 
    if (row_array & int(bin(2**length),base=2)>>(seat_num) == 0):
        return True
    return False

def register_ticket(match,segment,row,seat_num):
    seg, row_array, length= get_seats_and_prepare_for_binary(match,segment,row)
    row_array = row_array | int(bin(2**length),base=2)>>(seat_num)
    seg[row]=row_array
    if set_match_seat(match,segment,**seg) is not None:
        return True
    return False
