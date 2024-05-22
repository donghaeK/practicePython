'''
파이썬 실력 증진을 위한
2024 05 22 https://wikidocs.net/7014 파이썬 300문제 시작
'''

#111 사용자로부터 입력받은 문자열을 두 번 출력하라.
#아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
# input = input()
# print(input*2)

#112 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# input = input()
# print(int(input)+10)

#113 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# input = int(input())
# if input % 2 == 1:
#     print("홀수")
# else:
#     print("짝수")

#114 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라.
# 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
# input = int(input())
# if input < 255:
#     print(int(input+20))
# elif input >= 255:
#     print(255)

#115 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라.
# 단 출력 값의 범위는 0~255이다.
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
input = int(input())
if 0 <= input <= 255:
    print(input-20)
elif 0 > input:
    print(0)
elif input > 255:
    print(255)