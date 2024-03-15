import pyupbit
import os
import dotenv
from time import sleep

dotenv.load_dotenv()

access = os.environ['access_key']
secret = os.environ['secret_key']
upbit = pyupbit.Upbit(access, secret)

s = upbit.sell_market_order("KRW-ARB", 2)
sleep(0.1)
won = int(upbit.get_order(s['uuid'])['trades'][0]['funds'])
print(won)

b = upbit.buy_market_order("KRW-SOL", 5000)
sleep(0.1)
won = '0'
coin = int(upbit.get_order(s['uuid'])['trades'][0]['volume'])
print(coin)