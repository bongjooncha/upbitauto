import pyupbit
import os, dotenv

dotenv.load_dotenv()
access = os.environ['access_key']
secret = os.environ['secret_key']
upbit = pyupbit.Upbit(access, secret)

#지갑 내 얼마 있는지 확인
def my_wallet():
    #.get_balance는 지갑안에 얼마있는지 불러옴
    wallet = upbit.get_balances()
    wallet_list = []
    sum = 0
    for i in wallet:
        a = i['currency']
        number = float(i['balance'])
        if a == 'KRW':
            price = 1
            wallet_list.insert(0,[a,number,float(price) *number])
        else:
            price = pyupbit.get_current_price("KRW-"+a)
            wallet_list.append([a,number,float(price) *number])
        sum += float(price) *number
        #.get_current_price는 가장 최근 거래된 현재가를 조회
    formatted_total_price = "{:,.2f}".format(sum)
    print()
    print("총", formatted_total_price, "원")

    for i in wallet_list:
        if i == wallet_list[0]:  # 첫 번째 리스트일 경우 스킵
            print(i[0], "{:,.2f}".format(i[2]),'원')
            continue
        else: print("{}코인은 {}개({}원)".format(i[0], i[1], "{:,.2f}".format(i[2])))
    print()

    return wallet_list