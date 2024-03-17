import requests

url = "https://api.upbit.com/v1/market/all?isDetails=true"
headers = {"accept": "application/json"}
res = requests.get(url, headers=headers)

data = res.json()
# print(data)

n=0
for item in data:
    if item["market"].startswith("KRW-"):
        print("Market:", item["market"])
        print("Korean Name:", item["korean_name"])
        n= n +1

print(n)