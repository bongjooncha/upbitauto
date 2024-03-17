import pymysql
import os
import dotenv

    #db에 연결 및 cursor생성
def db_S(x):
    dotenv.load_dotenv()

    db_url = os.environ['aws_rds']
    db_user = os.environ['aws_rds_user']
    db_pw = os.environ['aws_rds_pw']

    schema = x

    db = pymysql.connect(host= db_url ,user=db_user, password=db_pw ,charset='utf8', database=schema)

    return db
