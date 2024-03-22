from apiuse.API.order import auto_buy,auto_sell
from apiuse.API.get_name import order_check
from apiuse.API.get_price import Candles
import uuid,datetime
from time import sleep

t = str(datetime.datetime.now())
now = t[:10]+'T'+t[11:19]
# print(now)

Candles.min(15,'KRW-BTC',now,10)