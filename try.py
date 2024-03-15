from API.order import auto_buy,auto_sell
from API.get_name import order_check
import uuid
from time import sleep

coin_name = 'ARB'
won = '5000'
coin = '0'

d = auto_buy("KRW-"+coin_name,won,'')
won = '0'
sleep(0.03)
print(order_check(d['uuid'])['trades'][0]['volume'])

d=auto_sell("KRW-"+coin_name,'',coin)
print(d)
sleep(0.5)
won = order_check(d['uuid'])['trades'][0]['funds']
print(won)
