'''
파이썬 실력 증진을 위한
2024 05 31 ~ 2024 06 02 https://wikidocs.net/7014 파이썬 300문제 시작
'''

#156  리스트에서 소문자만 화면에 출력하라.
리스트 = ["A", "b", "c", "D"]
#b
#c
for i in 리스트:
    if i.islower() == True:
        print(i)

# 157
# 이름의 첫 글자를 대문자로 변경해서 출력하라.
#
리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot
for i in 리스트:
       print(i[0].upper() + i[1:])

# 158
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)
#
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro
for i in 리스트:
    split = i.split(".")
    print(split[0])

# 159
# 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
#
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# define.h
for i in 리스트:
    split = i.split(".")
    if split[1] == "h":
        print(i)

# 160
# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
#
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# intra.c
# define.h
for i in 리스트:
    split = i.split(".")
    if split[1] == "h" or split[1] == "c":
        print(i)

#161 for문과 range 구문을 사용해서 0~99까지
# 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.
for i in range(100):
    print(i)

# 162
# 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
#
# 2002
# 2006
# 2010
# ...
# 2042
# 2046
# 2050
for i in range(2002, 2051, 4):
    print(i)

# 163
# 1부터 30까지의 숫자 중 3의 배수를 출력하라.
#
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30
for i in range(1, 31):
    if i % 3 == 0:
        print(i)

# 164
# 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
for i in range(99, -1, -1):
    print(i)

# 165
# for문을 사용해서 아래와 같이 출력하라.
#
# 0.0
# 0.1
# 0.2
# 0.3
# 0.4
# 0.5
# ...
# 0.9
for i in range(10):
    print(i / 10)

# 166
# 구구단 3단을 출력하라.
#
# 3x1 = 3
# 3x2 = 6
# 3x3 = 9
# 3x4 = 12
# 3x5 = 15
# 3x6 = 18
# 3x7 = 21
# 3x8 = 24
# 3x9 = 27
for i in range(1,10):
    print("3 X",i, "=", 3*i)

# 167
# 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.
#
# 3x1 = 3
# 3x3 = 9
# 3x5 = 15
# 3x7 = 21
# 3x9 = 27
for i in range(1, 10):
    if i % 2 ==1:
        print("3 X", i, "=", 3 * i)

# 168
# 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
# 다른방법
# total_sum = sum(range(1, 11))
# print(total_sum)
total_sum = 0
for i in range(1, 11):
    total_sum += i
print("합 :", total_sum)

# 169
# 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
total_sum = 0
for i in range(1, 11):
    if i % 2 == 1:
        total_sum += i
print("합 :", total_sum)

# 170
# 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
result = 1
for i in range(1, 11):
    result *= i
print(result)

