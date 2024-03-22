import pyupbit
import os, datetime, dotenv
from time import sleep
from index.momentum import h_index

dotenv.load_dotenv()

access = os.environ['access_key']
secret = os.environ['secret_key']
upbit = pyupbit.Upbit(access, secret)

coin_name = 'ARB'        #어떤 코인
ticker = 15             #몇분봉
won = '0'          #얼마를 자동 매매 시스템에 돌릴건지
coin = '37'
                        #자동매매기준
state = 1               #0 매수 대기상태, 1 매도대기 상태

print(upbit.get_balances())


'''
while True:
    sleep(0.3)
    t = str(datetime.datetime.now())
    now = t[:10]+'T'+t[11:19]

    #코인 가격 list에 저장
    candle = Candles().min(ticker,"KRW-"+coin_name,now,30)
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

    alert = datetime.datetime.now()

    if alert.minute % 5 == 0 and alert.second == 0:
        print([rsi[0] - rsi[1],sto_fast[0] - sto_fast[1],sto_slow[0] - sto_slow[1]])


    if state == 1 and sig >=2:        #매도 대기
        # print(state,sig)
        continue

    elif state == 0 and sig>=2:        #매수
        print([rsi[0] - rsi[1],sto_fast[0] - sto_fast[1],sto_slow[0] - sto_slow[1]])
        b = upbit.buy_market_order("KRW-"+coin_name, won)
        print(b)
        sleep(0.1)
        print(upbit.get_order(b['uuid']['trades'][0]))
        print(upbit.get_order(b['uuid']['trades'][0]['volume']))
        coin = round(float(upbit.get_order(b['uuid'])['trades'][0]['volume']),2)
        state = 1
        won = '0'
        print(coin, '개 매수 완료')
        continue

    elif state == 1 and sig < 2:       #매도
        print([rsi[0] - rsi[1],sto_fast[0] - sto_fast[1],sto_slow[0] - sto_slow[1]])
        s = upbit.sell_market_order("KRW-"+coin_name, coin)
        state = 0
        coin = '0'
        sleep(0.1)
        won = round(float(upbit.get_order(s['uuid'])['trades'][0]['funds']))
        print(won,'원 매도 완료')
        continue

    else:                            #매수 대기
        # print(state,sig)
        continue

'''