import redis
import json

"""
redis management class 
save and retrieve data from redis
"""

redis_client = redis.Redis(
     host= 'cache', 
     port= '6379',
     db=0)


def get_match_seats(name: str, segment: str) -> dict :
     botids = redis_client.hget(name, segment)
     return json.loads(botids)


def set_match_seat(name: str, segment: str, **kwargs) -> bool :
     resp = redis_client.hset(name,segment,json.dumps(kwargs))  
     return resp

