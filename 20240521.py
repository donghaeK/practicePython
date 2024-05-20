'''
파이썬 실력 증진을 위한
2024 05 21 https://wikidocs.net/7014 파이썬 300문제 시작
'''

#106 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
#print(3 => 4)
#정수형계산에서 3이 4보다 크거나 같지 않기때문이다.
#python에서는 지원하지 않는 연산자이다. 따라서 error

#107 아래 코드의 출력 결과를 예상하라
# if 4 < 3:
#     print("Hello World")
#Error
#조건만족X 아무것도 출력되지 않는다.

#108 아래 코드의 출력 결과를 예상하라
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")
#Hi, there.

#109 아래 코드의 출력 결과를 예상하라
# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")
#문자열은 True반환
#따라서
#1
#2
#4

#110 아래 코드의 출력 결과를 예상하라
#if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")
#3
#5
