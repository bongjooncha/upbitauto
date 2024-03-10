class h_index:
    

    #RSI 지표
    def calculate_rsi(data,period,av):     #data는 가격 데이터, period는 rsi 기간, av는 이평 데이터
        
        abs_A = []      #봉의 시작가-최종가 저장
        n = 0
        while n < period + av:
            for i in data:
                A = i[0]-i[3]
                abs_A.append(A)
                n= n+1

        rsi = []        #rsi 값 계산
        for i in 5:
            for abs in abs_A:
                print(abs)




        print(abs_A)
        # return rsi