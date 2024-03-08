import requests

url = "https://api.upbit.com/v1/candles/minutes/1?market=KRW-BTC&to=2024-03-07T00:00:00&count=5"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)


print(response.text)