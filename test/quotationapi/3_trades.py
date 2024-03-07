import requests

url = "https://api.upbit.com/v1/trades/ticks?market=KRW-BTC&count=1&count=1"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)