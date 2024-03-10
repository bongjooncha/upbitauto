import requests

#upbit 코인명 불러오기
def name():
    url = "https://api.upbit.com/v1/market/all?isDetails=true"
    headers = {"accept": "application/json"}
    res = requests.get(url, headers=headers)

    return res.json()

