import requests

class Candles():
    url = "https://api.upbit.com/v1/candles/"
    headers = {"accept": "application/json"}

    def min(self,market,to,count):
        url = self.url + "minutes/1?market={}&to={}&count={}".format(market,to,count)
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def hour(self,market,to,count):
        url = self.url + "minutes/60?market={}&to={}&count={}".format(market,to,count)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def day(self,market,to,count):
        url = self.url + "days?market={}&to={}&count={}".format(market,to,count)
        response = requests.get(url, headers=self.headers)
        return response.json()