class h_index:
    

    #RSI 지표
    def calculate_rsi(data,period,av):     #data는 가격 데이터, period는 rsi 기간, av는 이평 데이터
        
        gap_All = []      #봉의 시작가-최종가 저장
        n = 0
        while n < period + av:
            for i in data:
                A = i[0]-i[3]
                gap_All.append(A)
                n= n+1

        rsi = []        #rsi 값 저장
        n = 0
        while n < av:
            select_abs = gap_All[n:period+n]
            u = sum(num for num in select_abs if num>=0)
            d = sum(abs(num) for num in select_abs if num<0)
            rsi.append(u/(u + d) * 100)
            n = n+1

        return rsi[0],sum(rsi)/av