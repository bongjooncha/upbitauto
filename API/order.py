import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote
import dotenv

dotenv.load_dotenv()

access_key = os.environ['access_key']
secret_key = os.environ['secret_key']
server_url = os.environ['server_url']

m = hashlib.sha512()

#자산 현황
def get_wallet():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
    'Authorization': authorization,
    }

    params= {}

    res = requests.get(server_url + '/v1/accounts', params=params, headers=headers)

    origin_data = res.json()

    data = []

    for item in origin_data:
        currency = item['currency']
        balance = item['balance']
        avg_buy_price = item['avg_buy_price']
        data.append([currency, balance, avg_buy_price])

    return data

#주문
def execute_order(market, side, ord_type, price, volume):
    params = {
        'market': market,
        'side': side,
        'ord_type': ord_type,
        'price': price,
        'volume': volume
    }

    query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorization = 'Bearer {}'.format(jwt_token)
    headers = {
        'Authorization': authorization,
    }

    res = requests.post(server_url + '/v1/orders', json=params, headers=headers)
    return res.json()

def auto_buy(market, price, volume): #market=모살건지, price=얼마나 살건지
    return execute_order(market, 'bid', 'price', price, '')

def auto_sell(market, price, volume): # volume = 얼마나 팔건지
    return execute_order(market, 'ask', 'market','', volume)
