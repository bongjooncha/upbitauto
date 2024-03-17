import requests

class Candles():
    url = "https://api.upbit.com/v1/candles/"
    headers = {"accept": "application/json"}

    def min(self,minutes,market,to,count):
        url = self.url + "minutes/{}?market={}&to={}&count={}".format(minutes,market,to,count)
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