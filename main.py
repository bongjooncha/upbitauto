import datetime
from API.order import get_wallet,auto_buy,auto_sell
from API.get_price import Candles
from index.momentum import h_index
from time import sleep


while True:
    sleep(0.3)
    t = str(datetime.datetime.now())
    now = t[:10]+'T'+t[11:19]

    #코인 가격 list에 저장
    candle = Candles().min(15,"KRW-SOL",now,30)
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

    wallet = get_wallet()
    
    for item in wallet:
        if item[0] == 'SOL':
            sol_vol = item[1]
            break

    for item in wallet:
        if item[0] == 'KRW':
            krw_vol = item[1]
            break

    state=0
    for item in wallet:
        if item[0] == 'SOL':
            state = 1
            break

    if state == 1 & sig >=2: continue

    elif state == 0 & sig>=2:
        auto_buy("KRW-SOL",krw_vol,'')
        continue

    elif state == 1 & sig < 2:
        auto_sell("KRW-SOL",'',sol_vol)
        continue

    else: continue
        