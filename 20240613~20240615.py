'''
파이썬 실력 증진을 위한
2024 06 13 ~ 15 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 216
# 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
#
def print_with_smile(a):
    print(a+":D")
print_with_smile("안녕하세요")

# 217
# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
#
def print_upper_price(a):
    print(a*1.3)
print_upper_price(10000)
# 218
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
#
def print_sum(a,b):
    print(a+b)
print_sum(10,20)
# 219
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.

def print_arithmetic_operation(a,b):
    print(a,"+",b,"=",a+b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)
print_arithmetic_operation(3,4)
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75

# 220
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
def print_max(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
print_max(1,4,3)

# 221
# 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
#
# print_reverse("python")
# nohtyp
def print_reverse(a):
    print(a[::-1])
print_reverse("abc")
# 222
# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
#

# 2.0
def print_score(a):
    print(sum(a)/len(a))
print_score([1, 2, 3])
# 223
# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
#
# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12
def print_even(a):
    for x in a:
        if x % 2 == 0:
            print(x)
print_even([1, 3, 2, 10, 12, 11, 15])
# 224
# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
#
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별
def print_keys(a):
    for i in a.keys():
        print(i)
print_keys({"이름":"김말똥", "나이":30, "성별":0})
# 225
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
#
my_dict = {"10/26" : [100, 130, 100, 100],
            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
#
# [100, 130, 100, 100]
def print_value_by_key(my_dict, a):
    print(my_dict[a])
print_value_by_key(my_dict, "10/26")

# 226
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
#
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸
def print_5xn(a):
    num = int(len(a)/5)
    for i in range(num+1):
        print(a[i*5:i*5+5])
print_5xn("아이엠어보이유알어걸")
# 227
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
#
# 아이엠
# 어보이
# 유알어
# 걸
def printmxn(a,b):
    num = int(len(a) / b)
    for i in range(num+1):
        print(a[i*b:i*b+b])
printmxn("아이엠어보이유알어걸", 3)
# 228
# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
def calc_monthly_salary(a):
    monthly_pay = int(a / 12)
    return monthly_pay
calc_monthly_salary(12000000)
# 1000000

# 229
# 아래 코드의 실행 결과를 예측하라.
#
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(a=100, b=200)
#왼쪽:100
#오른쪽:200
# 230
# 아래 코드의 실행 결과를 예측하라.
#
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
#
# my_print(b=100, a=200)
#왼쪽:200
#오른쪽:100
