class h_index:
    
    #RSI 지표
    def calculate_rsi(data,period,av):     #data는 가격 데이터, period는 rsi 기간, av는 이평 데이터
        trade_price = [num[3] for num in data]

        gap_All = []      #당일 최종가-전일 최종가 저장

        for i in range(period + av + 1):
            gap_All.append(trade_price[i]-trade_price[i+1])

        rsi = []        #rsi 값 저장
        n = 0
        
        while n < av:
            select_abs = gap_All[n+1:period+n+2]
            u_p = sum(num for num in select_abs if num>0)/period
            d_p = sum(num for num in select_abs if num<0)/period
            if gap_All[n]>=0:
                u = ((u_p * 13) + gap_All[n])/14
                d = d_p * 13 / 14
            else: 
                u = u_p * 13 / 14
                d = ((d_p * 13) + gap_All[n]) / 14
            rs = u/d
            rsi.append(100-(100/(1-rs)))
            n = n+1

        # while n < av:
        #     select_abs = gap_All[n:period]
        #     u = sum(num for num in select_abs if num>0)/period
        #     d = sum(num for num in select_abs if num<0)/period

        #     rs = u/d
        #     rsi.append(100-(100/(1-rs)))
        #     n = n+1

        rsi_av = sum(rsi)/av

        return rsi[0],rsi_av       #현재 rsi값, rsi의 av 이평값
    
    #fast 스토케스틱 지표
    def stocastic_fast(data,period,av):
        K_All = []
        n=0
        while n < av:
            lowest_price = min([num[2] for num in data[n:period + n]])
            highest_price = max([num[1] for num in data[n:period + n]])
            end_price = data[n][3]
            K=(end_price - lowest_price)/(highest_price - lowest_price) * 100

            K_All.append(K)
            n = n+1

        return K_All[0],sum(K_All)/av   #K 값, K의 av 이평값

    #slow 스토케스틱 지표
    def stocastic_slow(data,period,av1,av2):

        n2 = 0
        K_All = []

        while n2 < av2:
            F_K_All = []
            n1=0

            while n1 < av1:
                lowest_price = min([num[2] for num in data[n1 + n2:period + n1 + n2]])
                highest_price = max([num[1] for num in data[n1 + n2:period + n1 + n2]])
                end_price = data[n1 + n2][3]
                K=(end_price - lowest_price)/(highest_price - lowest_price) * 100

                F_K_All.append(K)
                n1 = n1+1
            K_All.append(sum(F_K_All)/av1)
            n2 = n2+1
        
        return K_All[0],sum(K_All)/av2   #K 값, K의 av 이평값