import requests

url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)