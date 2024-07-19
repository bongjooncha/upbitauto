import pyupbit
import os, datetime, dotenv
from apiuse.API.get_price import Candles
from pyupbit_plus.myfunc import my_wallet
from time import sleep

dotenv.load_dotenv()
access = os.environ['access_key']
secret = os.environ['secret_key']
upbit = pyupbit.Upbit(access, secret)

coin_name = 'SOL'
won = 5010
coin = 0.0225

trade = upbit.sell_market_order('KRW-'+coin_name, coin)
uuid = trade['uuid']
sleep(0.1)
coin = float(upbit.get_order(uuid)['trades'][0]['volume'])
won = float(upbit.get_order(uuid)['trades'][0]['funds'])- float(upbit.get_order(uuid)['paid_fee'])
print(uuid, coin, won)