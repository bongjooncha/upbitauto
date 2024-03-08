import pymysql

db = pymysql.connect(host='localhost',user='root', password='12345678',charset='utf8')

cursor = db.cursor()
cursor.execute('')
print(db)