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

# print(price)


# print(price[0])
# print(h_index.calculate_rsi(price,14,9))

print(h_index.stocastic_fast(price,5,3))
print(h_index.stocastic_slow(price,3,3))