import pyupbit
import os
import dotenv

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