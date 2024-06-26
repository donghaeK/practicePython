'''
파이썬 실력 증진을 위한
2024 06 08 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 196
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.
#
ohlc = [["open", "high", "low", "close"],
         [100, 110, 70, 100],
         [200, 210, 180, 190],
         [300, 310, 300, 310]
]
# 190
# 310
for i in ohlc[1:4]:
    for x in i[3:4]:
        if x > 150 :
            print(x)

# 197
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.
#
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 100
# 310
print("====")
for i in ohlc[1:]:
    if i[3] >= i[0]:
        print(i[3])

# 198
# ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다.
# 고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.
#
ohlc = [["open", "high", "low", "close"],
         [100, 110, 70, 100],
         [200, 210, 180, 190],
         [300, 310, 300, 310]]
# >> print(volatility)
# [40, 30, 10]
print("====")
volatility = []
for i in ohlc[1:]:
    v = i[1] - i[2]
    volatility.append(v)
print(volatility)

# 199
# 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.
#
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 종가가 시가보다 높은 거래일의 OHLC는 [300, 310, 300, 310] 이다. 따라서 이 거래일의 변동성은 10 (310 - 300)이다.
#
# 10
print("====")
for i in ohlc[1:]:
    if i[3] - i[0] > 0:
        print(i[1]-i[2])

# 200
# 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.
#
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 1일차 수익 0원 (100 - 100), 2일차 수익 -10원 (190 - 200), 3일차 수익 10원 (310 - 300) 이다.
#
# 0
print("====")
charge = 0
for i in ohlc[1:]:
    charge += i[3] - i[0]
print(charge)


