import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

path = jwt

access_key = os.environ[path]
secret_key = os.environ[path]
server_url = os.environ[path]

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