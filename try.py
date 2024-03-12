from API.order import get_wallet,auto_buy,auto_sell

wallet = get_wallet()
print(wallet)

for item in wallet:
    if item[0] == 'SOL':
        sol_vol = item[1]
        break

for item in wallet:
    if item[0] == 'KRW':
        krw_vol = item[1]
        break


# a= auto_sell("KRW-SOL",'500000.0',sol_vol)
a=auto_buy("KRW-SOL",'5000','')
print(a)