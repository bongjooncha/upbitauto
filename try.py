import datetime
from API.get_price import Candles
from index.line import h_index

t = str(datetime.datetime.now())
time = t[:10]+'T'+t[11:19]

#코인 가격 list에 저장
candle = Candles().min(5,"KRW-BTC",time,30)
price = []
for c in candle:
    price.append([c['opening_price'],c['high_price'],c['low_price'],c['trade_price']])


print(price[0])
print(h_index.calculate_rsi(price,14,9))
# rsi_value = calculate_rsi(price)
# print("RSI 지표:", rsi_value)