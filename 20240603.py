'''
파이썬 실력 증진을 위한
2024 06 03 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 171
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
price_list = [32100, 32150, 32000, 32500]
# 32100
# 32150
# 32000
# 32500
for i in range(4):
    print(price_list[i])

# 172
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
# price_list = [32100, 32150, 32000, 32500]
# 0 32100
# 1 32150
# 2 32000
# 3 32500
for i, data in enumerate(price_list):
    print(i, data)

# 173
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
# price_list = [32100, 32150, 32000, 32500]
# 3 32100
# 2 32150
# 1 32000
# 0 32500
for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])

print("====")
# 174
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
#
# price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500
for i, data in enumerate(price_list[1:]):
    print(i*10+100, data)

# 175
# my_list를 아래와 같이 출력하라.
#
my_list = ["가", "나", "다", "라"]
# 가 나
# 나 다
# 다 라
for i in range(3):
    print(my_list[0+i:2+i])