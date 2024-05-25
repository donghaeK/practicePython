'''
파이썬 실력 증진을 위한
2024 05 25 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 126
# 우편번호는 5자리로 구성되는데,앞의 세자리는 구를 나타낸다.
# 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라

# inp = (input("우편번호:" ))
# print(inp[2])
# if inp[2] == "0" or "1" or "2":
#     print("강북구")
# elif inp[2] == "3" or "4" or "5":
#     print("도봉구")
# elif inp[2] == "6" or "7" or "8" or "9":
#     print("노원구")
# else:
#     print("없는지역입니다.")

#답안, keyword:in
# 우편번호 = input("우편번호: ")
# 우편번호 = 우편번호[:3]
# if 우편번호 in ["010", "011", "012"]:
#     print("강북구")
# elif 우편번호 in ["014", "015", "016"]:
#     print("도봉구")
# else:
#     print("노원구")

#127 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데,
#1, 3은 남자 2, 4는 여자를 의미한다.
#사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
#inp1 = input("주민등록번호: ")
#inp1 = inp1.split("-")
# print(inp1[1][0])
# if inp1[1][0] == "1" or inp1[1][0] == "3":
#     print("남자")
# elif inp1[1][0] == "2" or inp1[1][0] == "4":
#     print("여자")

#128 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# inp2 = inp1[1][1]
# if inp2 in ["0","1","2","3","4","5","6","7","8"]:
#     print("서울 입니다.")
# elif inp2 in ["8","9"]:
#     print("서울이 아닙니다.")

#129 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
#먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤
#그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가 나오는데
#11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
# calculate = int(inp1[0]) * 2 + int(inp1[1]) * 3 + int(inp1[2]) * 4 + int(inp1[3]) * 5 + int(inp1[4]) * 6 + \
#         int(inp1[5]) * 7 + int(inp1[7]) * 8 + int(inp1[8]) * 9 + int(inp1[9]) * 2 + int(inp1[10])* 3 + \
#         int(inp1[11])* 4 + int(inp1[12]) * 5
# calculate2 = 11 - (calculate % 11)
# calculate3 = str(calculate2)
# if inp1[-1] == calculate3:
#     print("유효한 주민등록번호입니다.")
# else:
#    print("유효하지 않은 주민등록번호입니다.")

#130 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다.
# 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우
# "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.
print(btc)
print(btc["opening_price"])
x = int(btc["max_price"]) + int(btc["min_price"])
y = x + int(btc["opening_price"])
if y > int(btc["max_price"]):
    print("상승장")
elif y < int(btc["max_price"]):
    print("하락장")