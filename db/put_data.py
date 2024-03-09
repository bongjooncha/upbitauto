from db_conect import db_S
from get_price import Candles
from get_name import name
import time

#db연결
db = db_S("coin_day")
cursor = db.cursor()

#이름 데이터 불러오기
coin_name = name()

#마지막 시간 설정
end_time = "2024-03-08T00:00:00"

for item in coin_name:
    if item["market"].startswith("KRW-"):
        market = item["market"].replace('-','_')
        korean_name = item["korean_name"]
        table_name = f"{market}_{korean_name}"  # 테이블 이름
        day = Candles().day(item["market"], end_time, "200")
        time.sleep(1)

        for data in day:
            candle_date_time_kst = data["candle_date_time_kst"]
            opening_price = data["opening_price"]
            high_price = data["high_price"]
            low_price = data["low_price"]
            trade_price = data["trade_price"]
            volume_price = data["candle_acc_trade_price"]
            volume = data["candle_acc_trade_volume"]
            insert_query = f"""
            INSERT INTO `{table_name}` (time, open_price, high_price, low_price, trade_price, volume, volume_price) 
            VALUES ('{candle_date_time_kst}', {opening_price}, {high_price}, {low_price}, {trade_price}, {volume}, {volume_price})
            """

            cursor.execute(insert_query)

db.commit()
cursor.close()
db.close()
