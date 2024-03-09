from db_conect import db_S
import requests

#db에 연결 및 cursor생성
db = db_S("coin_day")
cursor = db.cursor()

#upbit 코인명 불러오기
url = "https://api.upbit.com/v1/market/all?isDetails=true"
headers = {"accept": "application/json"}
res = requests.get(url, headers=headers)

data = res.json()



# 테이블 생성 및 데이터 추가
for item in data:
    if item["market"].startswith("KRW-"):
        market = item["market"].replace('-','_')
        korean_name = item["korean_name"]
        table_name = f"{market}_{korean_name}"  # 테이블 이름 생성

        # 테이블 생성 쿼리
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            time DATETIME,
            open_price DECIMAL(20,8),
            high_price DECIMAL(20,8),
            low_price DECIMAL(20,8),
            trade_price DECIMAL(20,8),
            volume DECIMAL(20,8),
            volume_price DECIMAL(20,8)
        )
        """
        # 테이블 생성 쿼리 실행
        cursor.execute(create_table_query)

# 변경사항을 커밋하여 데이터베이스에 반영
db.commit()

# 작업 완료 후 연결 종료
cursor.close()
db.close()