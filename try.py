import datetime
from API.order import get_wallet,auto_buy,auto_sell
from API.get_price import Candles
from index.momentum import h_index
from time import sleep

coin = 'SOL'            #어떤 코인
ticker = 15             #몇분봉
won = '100000'          #얼마를 자동 매매 시스템에 돌릴건지

                        #자동매매기준
state = 0               #0 매수 대기상태, 1 매도대기 상태


t = str(datetime.datetime.now())
now = t[:10]+'T'+t[11:19]

#코인 가격 list에 저장
candle = Candles().min(ticker,"KRW-"+coin,now,30)
price = []
for c in candle:
    price.append([c['opening_price'],c['high_price'],c['low_price'],c['trade_price']])

    
rsi = h_index.calculate_rsi(price,14,9)
sto_fast = h_index.stocastic_fast(price,5,3)
sto_slow = h_index.stocastic_slow(price,5,3,3)

#매수 매도 상황 결정
rsi_sig = 1 if rsi[0] > rsi[1] else 0
sto_fast_sig = 1 if sto_fast[0] > sto_fast[1] else 0
sto_slow_sig = 1 if sto_slow[0] > sto_slow[1] else 0

sig = rsi_sig + sto_fast_sig + sto_slow_sig
print([rsi[0] - rsi[1],sto_fast[0] - sto_fast[1],sto_slow[0] - sto_slow[1]])


if state == 1 & sig >=2: 
    print('매도 대기')

elif state == 0 & sig>=2:
    auto_buy("KRW+"+coin,krw_vol,'')

elif state == 1 & sig < 2:
    auto_sell("KRW+"+coin,'',sol_vol)
    print(sol_vol,'매도')

else:
    print('매수 대기')
    