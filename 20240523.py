'''
파이썬 실력 증진을 위한
2024 05 23 https://wikidocs.net/7014 파이썬 300문제 시작
'''

#116 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# >> 현재시간:02:00
# 정각 입니다.
# >> 현재시간:03:10
# 정각이 아닙니다
time = input("현재시간:")
if time[-2:] == "00":
    print("정각입니다.")
else:
    print("정각이 아닙니다.")

#117 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라.
#포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
input0 = input()
fruit = ["사과", "포도", "홍시"]
if input0 in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

#118투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면
# '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
input1 = input()
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
if input1 in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

#119아래와 같이 fruit 딕셔너리가 정의되어 있다.
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면
# "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
input2 = input()
if input2 in fruit.keys():
    print("정답입니다.")
else:
    print("오답입니다.")

#120아래와 같이 fruit 딕셔너리가 정의되어 있다.
# 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면
# "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
input3 = input()
if input3 in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
