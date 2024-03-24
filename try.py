from apiuse.API.order import auto_buy,auto_sell
from apiuse.API.get_name import order_check
from apiuse.API.get_price import Candles
import uuid,datetime,dotenv,os
from time import sleep
import pyupbit

dotenv.load_dotenv()
access = os.environ['access_key']
secret = os.environ['secret_key']
upbit = pyupbit.Upbit(access, secret)
pre_coin = upbit.get_balance('BTC')
print(pre_coin)