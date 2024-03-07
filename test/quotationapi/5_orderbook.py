import requests

url = "https://api.upbit.com/v1/orderbook?markets=KRW-BTC,KRW-ETH&level=10000"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)