'''
파이썬 실력 증진을 위한
2024 05 16 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 081 별 표현식
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다.
# 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다.
# 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
#>> a, b, *c = (0, 1, 2, 3, 4, 5)
#>> a
#0
#>> b
#1
#>> c
#[2, 3, 4, 5]
#다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여
# 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
#*a, b, c = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# valid_score = a
# print(valid_score)
*valid_score, _, _ = scores
print(valid_score)

#082 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때,
# start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
_,_,*valid_score = scores
print(valid_score)

#083다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때,
# start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
_, *valid_score, _ = scores
print(valid_score)

#084 비어있는 딕셔너리
# temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}

#085 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
#icecream = {'메로나, 1000', '폴라포, 1200', '빵빠레, 1800'}
icecream = {'메로나':1000, '폴라포': 1200, '빵빠레': 1800}
print(icecream)
