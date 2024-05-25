'''
파이썬 실력 증진을 위한
2024 05 26 https://wikidocs.net/7014 파이썬 300문제 시작
'''

#131 for문의 실행결과를 예측하라.

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

# 사과 귤 수박

# 132 for문의 실행결과를 예측하라.
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")

# ##### ##### #####

#133 다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.
for 변수 in ["A", "B", "C"]:
  print(변수)

a = ["A", "B", "C"]
for i in a:
    print(i)

#134 for문을 풀어서 동일한 동작을하는 코드를 작성하라.

for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)

num = ["A", "B", "C"]
print("출력:", num)

#변수 = "A"
# print("출력:", 변수)
# 변수 = "B"
# print("출력:", 변수)
# 변수 = "C"
# print("출력:", 변수)
# print("출력:", "A")
# print("출력:", "B")
# print("출력:", "C")



#135 for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)


# x = ['A', 'B', 'C']
# print(x.lower())

#답안
# #변수 = "A"
# b = 변수.lower()
# print("변환:", b)
# 변수 = "B"
# b = 변수.lower()
# print("변환:", b)
# 변수 = "C"
# b = 변수.lower()
# print("변환:", b)