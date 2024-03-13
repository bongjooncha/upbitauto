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

params = {
  'market': 'KRW-SOL',
  'side': 'bid',
  'ord_type': 'limit',
  'price': '100000.0',
  'volume': '1'
}
query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

m = hashlib.sha512()
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
a = res.json()
print(a)
print(a['volume'])