import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
 
def get_popular_stocks():
    popular_stocks = []
    
    pattern = "BM:ADVICED:*"
    keys = r.keys(pattern)
    for key in keys:
        popular_stock = json.loads(r.get(key))
        popular_stocks.append(popular_stock)

    return popular_stocks

def get_user_watch_list():
    watch_list = []
    
    pattern = "STOCK:*"
    keys = r.keys(pattern)
    for key in keys:  
        popular_stocks.append(popular_stock)

    return popular_stocks


"""
mapping={"price": 5, "volume": 500}

"""