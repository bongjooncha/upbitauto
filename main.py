import pyupbit
import os, datetime, dotenv
from time import sleep
from index.momentum import h_index
from apiuse.API.get_price import Candles
from pyupbit_plus.myfunc import my_wallet

dotenv.load_dotenv()
access = os.environ['access_key']
secret = os.environ['secret_key']
upbit = pyupbit.Upbit(access, secret)

#얼마 있는지 확인
wallet = my_wallet()

#자동매매 변수 결정
ticker = '15'             #몇분봉
coin_name = 'arb'.upper()       #코인명
current_coin_num = next((coin_info[1] for coin_info in wallet if coin_info[0] == coin_name), 0)
current_coin_price = next((coin_info[2] for coin_info in wallet if coin_info[0] == coin_name), 0)

#0 매수 대기상태, 1 매도대기 상태
state = 1 #보유 원화로 시작(0), 보유 코인으로 시작(1)
if state == 0:
    won = '0' #얼마로 할것 인지 입력
    won = float(won)
    origin_won = won
    coin_num = 0
    if won > wallet[0][1]:
        print('입력한 금액이 보유 금액보다 큽니다.')
        exit()
else:
    won = 0
    coin_price = '100000' #코인 얼마치를 사용할 것인지 입력
    coin_price = float(coin_price) 
    origin_won = coin_price
    coin = coin_price/(pyupbit.get_current_price("KRW-"+coin_name))
    if coin_price > current_coin_price:
        print("보유한 코인 수가 적습니다.")
        exit()



while 0.7 * origin_won < won or 0.7*origin_won < coin_price:
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
        pre_won = upbit.get_balance('KRW')
        pre_coin = upbit.get_balance(coin_name)

        upbit.buy_market_order('KRW-'+coin_name, won*0.9995)
        sleep(0.1)

        aft_won = upbit.get_balance('KRW')
        aft_coin = upbit.get_balance(coin_name)

        coin = aft_coin - pre_coin
        won = pre_won - aft_won
        coin_price = coin * pyupbit.get_current_price("KRW-"+coin_name)

        state = 1
        print(coin_price,'원 매수, 현재 금액 원금 대비', coin_price / origin_won,'배')
        print()
        continue

    elif state == 1 and sig < 2:       #매도
        print([rsi[0] - rsi[1],sto_fast[0] - sto_fast[1],sto_slow[0] - sto_slow[1]])
        pre_won = upbit.get_balance('KRW')
        pre_coin = upbit.get_balance(coin_name)

        upbit.sell_market_order('KRW-'+coin_name, coin)
        sleep(0.1)

        aft_won = upbit.get_balance('KRW')
        aft_coin = upbit.get_balance(coin_name)

        coin = pre_coin - aft_coin
        won = aft_won - pre_won

        state = 0
        print(won,'원 매도, 현재 금액 원금 대비', won/origin_won,'배')
        print()
        continue

    else:                            #매수 대기
        # print(state,sig)
        continue