import jwt
import os
import requests
import uuid
from urllib.parse import urlencode, unquote
import dotenv

dotenv.load_dotenv()

access_key = os.environ['access_key']
secret_key = os.environ['secret_key']
server_url = os.environ['server_url']

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
res.json()

print(res.json())