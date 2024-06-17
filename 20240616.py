'''
파이썬 실력 증진을 위한
2024 06 16 ~ 17 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 231
# 아래 코드를 실행한 결과를 예상하라.
#
# def n_plus_1 (n) :
#     result = n + 1
#
# n_plus_1(3)
# print (result)
#4
#오답 리턴이발생함(함수내부접근불가, 접근하려면 return을 사용해야함)
# 232
# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
#
# make_url("naver")
# www.naver.com
def make_url(a):
    return "www." + a + ".com"

# 233
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
#
# make_list("abcd")
# ['a', 'b', 'c', 'd']
def make_list(b):
    alist = []
    for i in b:
        alist.append(i)
    return alist

# 234
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
#
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]
def pickup_even(c):
    alist = []
    for i in c:
        if i % 2 == 0:
            alist.append(i)
    return alist
# 235
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
#
# convert_int("1,234,567")
# 1234567
def convert_int(d):
    return int(d.replace(',',''))
convert_int("1,234,567")

# 236
# 아래 코드의 실행 결과를 예측하라.
#
# def 함수(num) :
#     return num + 4
#
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

#14
#18
#22

# 237
# 아래 코드의 실행 결과를 예측하라.
#
# def sdf(num) :
#      return num + 4
#
# c = sdf(sdf(sdf(10)))
# print(c)

#22

# 238
# 아래 코드의 실행 결과를 예측하라.
#
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     return num * 10
#
# a = 함수1(10)
# c = 함수2(a)
# print(c)

#140

# 239
# 아래 코드의 실행 결과를 예측하라.
#
# def 함수1(num) :
#     return num + 4
#
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
#
# c = 함수2(10)
# print(c)

#16

# 240
# 아래 코드의 실행 결과를 예측하라.
#
# def 함수0(num) :
#     return num * 2
#
# def 함수1(num) :
#     return 함수0(num + 2)
#
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
#
# c = 함수2(2)
# print(c)

#28