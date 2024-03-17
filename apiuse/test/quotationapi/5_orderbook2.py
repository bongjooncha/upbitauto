import requests

url = "https://api.upbit.com/v1/orderbook/supported_levels?markets=KRW-BTC"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)