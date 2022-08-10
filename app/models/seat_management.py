import redis
import json


redis_client = redis.Redis(
     host= 'cache', 
     port= '6379',
     db=0)



def get_match_seats(name,segment) :
     botids = redis_client.hget(name, segment)
     return json.loads(botids)

   

def set_match_seat(name,segment,**kwargs) -> bool :
     resp = redis_client.hset(name,segment,json.dumps(kwargs))     
     return resp


     
#debug mode
if __name__ == "__main__":
     # updatePrice('BCHUSDTM', 1839.383)
     print(get_pair_whitelist("5"))
     # getPrice('BCHUSDTM')
     # getAskPrice('SOLUSDTM')
