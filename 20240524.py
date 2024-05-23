'''
파이썬 실력 증진을 위한
2024 05 24 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 121 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로,
# 대문자 일 경우, 소문자로 변경해서 출력하라.
# input1 = input()
# if input1.islower() == True:
#     print(input1.upper())
# else:
#     print(input1.lower())

# 122 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
# 사용자로부터 score를 입력받아 학점을 출력하라.
# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E
# print("score: ")
# input2 = int(input())
# if 80 < input2 < 100:
#     print("grade is A")
# elif 60 < input2 < 80:
#     print("grade is B")
# elif 40 < input2 < 60:
#     print("grade is C")
# elif 20 < input2 < 40:
#     print("grade is D")
# elif 0 < input2 < 20:
#     print("grade is E")

#123 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후
# 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다.
# 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이
# 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# input3 = input()
# int_input = int(input3.split(" ")[0])
# if input3.split(" ")[-1] == "달러":
#     print(int_input * 1167)
# elif input3.split(" ")[-1] == "엔":
#     print(int_input * 1.096)
# elif input3.split(" ")[-1] == "유로":
#     print(int_input * 1268)
# elif input3.split(" ")[-1] == "위안":
#     print(int_input * 171)

#답안
# 환율 = {"달러": 1167,
#         "엔": 1.096,
#         "유로": 1268,
#         "위안": 171}
# user = input("입력: ")
# num, currency = user.split()
# print(float(num) * 환율[currency], "원")


# 124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# input4 = int(input("input number1: "))
#
# input5 = int(input("input number2: "))
#
# input6 = int(input("input number3: "))
#
# if input4 > input5 and input4 > input6:
#     print(input4)
# elif input5 > input4 and input5 > input6:
#     print(input5)
# elif input6 > input4 and input6 > input5:
#     print(input6)

# 125
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다.
# 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
input7 = input("휴대전화 번호 입력: ")
if input7[0:3] == "011":
    print("당신은 skt 사용자입니다.")
elif input7[0:3] == "016":
    print("당신은 kt 사용자입니다.")
elif input7[0:3] == "019":
    print("당신은 lgu 사용자입니다.")
else:
    print("당신은 알수없는 통신사입니다..")





