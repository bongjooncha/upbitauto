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

ticker = '15'             #몇분봉
coin_name = 'sol'.upper()       #코인명
current_coin_num = next((coin_info[1] for coin_info in wallet if coin_info[0] == coin_name), 0)
current_coin_price = next((coin_info[2] for coin_info in wallet if coin_info[0] == coin_name), 0)
uuid = 0

#0 매수 대기상태, 1 매도대기 상태, 2 매도 후 신호대기
state = 0 #보유 원화로 시작(0), 보유 코인으로 시작(1)
if state == 0:
    won = '10000' #얼마로 할것 인지 입력
    won = float(won)
    origin_won = won
    coin_num = 0
    coin = 0
    if won > wallet[0][1]:
        print('입력한 금액이 보유 금액보다 큽니다.')
        exit()
else:
    won = 0
    coin_price = '0' #코인 얼마치를 사용할 것인지 입력
    coin_price = float(coin_price) 
    origin_won = coin_price
    coin = coin_price/(pyupbit.get_current_price("KRW-"+coin_name))
    if coin_price > current_coin_price:
        print("보유한 코인 수가 적습니다.")
        exit()

while 0.7 * origin_won < won or 0.7*origin_won < won_v:
    sleep(0.3)
    t = str(datetime.datetime.now())
    now = t[:10]+'T'+t[11:19]
    candle = Candles().min(ticker,"KRW-"+coin_name,now,200)

    price = []
    for c in candle:
        price.append([c['opening_price'],c['high_price'],c['low_price'],c['trade_price']])

    current = price[0][3]
    five = h_index.moving_average(price,5)
    ten = h_index.moving_average(price,10)
    twenty = h_index.moving_average(price,20)
    fifty = h_index.moving_average(price,50)

    now = datetime.datetime.now()
    current_seconds = now.second
    if current_seconds == 0:
        a = current - five
        b = five - ten
        c = ten - twenty
        d = twenty - fifty
        print(now)
        print(f"a:{a}, b:{b}, c:{c}, d:{d}")
        if state == 0:
            print(f"매수 대기: 원화 {won}원")
        elif state == 1:
            print(f"매도 대기: 코인{coin}개, 원화 {won_v}원 어치")
        else:
            print(f"재진입 대기: 원화 {won}")
        print("----------")

    #매수 대기
    if state == 0 and (current>five or current >ten) and ten>twenty and twenty > fifty:
        state = 1
        trade = upbit.buy_market_order('KRW-'+coin_name, won*0.9995)
        uuid = trade['uuid']
        sleep(0.1)
        coin = float(upbit.get_order(uuid)['trades'][0]['volume'])
        won_v = float(upbit.get_order(uuid)['trades'][0]['funds'])- float(upbit.get_order(uuid)['paid_fee'])
        won = 0
        print(f"매수: 코인 {coin}개 {won_v}원 어치")

    #재진입 대기
    elif state == 2 and (current < five or current < ten or ten < twenty or twenty < fifty):
        state = 0 #매수 대기로 변경

    #매도 조건
    elif state ==1:
        #익절 조건
        if (current-five)>=2*(five-ten) or (current-five)>=current/250:
            state = 2
            trade = upbit.sell_market_order('KRW-'+coin_name, coin)
            uuid = trade['uuid']
            sleep(0.1)
            coin = 0
            prev_won = won
            won = float(upbit.get_order(uuid)['trades'][0]['funds'])- float(upbit.get_order(uuid)['paid_fee'])
            print(f"익절: 현재 {won}원, 이전은 {prev_won}원")

        #손절 조건
        elif current < ten:
            trade = upbit.sell_market_order('KRW-'+coin_name, coin)
            uuid = trade['uuid']
            sleep(0.1)
            coin = 0
            prev_won = won
            won = float(upbit.get_order(uuid)['trades'][0]['funds'])- float(upbit.get_order(uuid)['paid_fee'])
            print(f"손절: 현재 {won}원, 이전은 {prev_won}원")

        else:
            continue
