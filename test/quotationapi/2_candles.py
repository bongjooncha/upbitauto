import requests

url = "https://api.upbit.com/v1/candles/minutes/1?market=KRW-BTC&count=10"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)