import jwt   # PyJWT 
import uuid

payload = {
    'access_key': '발급받은 Access Key',
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, '발급받은 Secret Key')
authorization_token = 'Bearer {}'.format(jwt_token)


import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

path = jwt

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.get(server_url + '/v1/accounts', params=params, headers=headers)
res.json()