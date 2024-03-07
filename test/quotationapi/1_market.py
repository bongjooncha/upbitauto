import requests

url = "https://api.upbit.com/v1/market/all?isDetails=true"

headers = {"accept": "application/json"}

res = requests.get(url, headers=headers)

data = res.json()

print(res.json()) 

# markets = [item['market'] for item in data]

# print(markets)
# print('')
# bitcoin_info = [item for item in data if item['korean_name'] == '비트코인']

# print(bitcoin_info)