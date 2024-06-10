'''
파이썬 실력 증진을 위한
2024 06 11 ~ 12 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 211
# 함수의 호출 결과를 예측하라.
#
# def 함수(문자열) :
#     print(문자열)
#
# 함수("안녕")
# 함수("Hi")
def fuc1(a):
    print(a)
fuc1("안녕")
fuc1("Hi")
#안녕
#Hi

# 212
# 함수의 호출 결과를 예측하라.
#
# def 함수(a, b) :
#     print(a + b)
#
# 함수(3, 4)
# 함수(7, 8)
def fuc2(a,b):
    print(a+b)
fuc2(3,4)
fuc2(7,8)

# 213
# 아래와 같은 에러가 발생하는 원인을 설명하라.
#
# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'
# 함수에 쓰일 매개변수(문자열)이 없어서이다.

# 214
# 아래와 같은 에러가 발생하는 원인을 설명하라.
#
# def 함수(a, b) :
#     print(a + b)
#
# 함수("안녕", 3)
# TypeError: must be str, not int
# 함수에 매개변수로 오는 "안녕"은 문자열, 3은 정수형이므로 더할 수 없다.

# 215
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는
# print_with_smile 함수를 정의하라.
def print_with_smile(a):
    print(a+":D")

print_with_smile("a")
