'''
파이썬 실력 증진을 위한
2024 05 30 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 151
# 리스트에는 네 개의 정수가 저장돼 있다.
#
리스트 = [3, -20, -3, 44]
# for문을 사용해서 리스트의 음수를 출력하라.
#
# -20
# -3
for i in 리스트:
    if i< 0:
        print(i)

# 152
# for문을 사용해서 3의 배수만을 출력하라.
#
리스트 = [3, 100, 23, 44]
# 3
for i in 리스트:
    if i % 3 == 0:
        print(i)

# 153
# 리스트에서 20 보다 작은 3의 배수를 출력하라
#
리스트 = [13, 21, 12, 14, 30, 18]
# 12
# 18
for i in 리스트:
    if i <20 and i % 3 == 0:
        print(i)

# 154
# 리스트에서 세 글자 이상의 문자를 화면에 출력하라
#
리스트 = ["I", "study", "python", "language", "!"]
# study
# python
# language
for i in 리스트:
    if len(i) >= 3:
        print(i)

# 155
# 리스트에서 대문자만 화면에 출력하라.
#
리스트 = ["A", "b", "c", "D"]
# A
# D
# (참고) isupper() 메서드는 대문자 여부를 판별합니다.
#
# >> 변수 = "A"
# >> 변수.isupper()
# True
# >> 변수 = "a"
# >> 변수.isupper()
# False
for i in 리스트:
    if i.isupper():
        print(i)