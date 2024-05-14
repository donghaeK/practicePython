'''
파이썬 실력 증진을 위한
2024 05 15 https://wikidocs.net/7014 파이썬 300문제 시작
'''

#076 변수 t에는 아래와 같은 값이 저장되어 있다.
# 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
t = ('A', 'B', 'C')
print(t)
#?

#077 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(data)

#078 다음 리스트를 튜플로 변경하라.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# print(interest)
data = tuple(interest)

#079 튜플 언팩킹 다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
#오류?
#apple banana cake

#080 range 함수 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# for i in range(2, 99, 2):
#     tup = (i)
# print(tup)
data = tuple(range(2,100,2))
print(data)

