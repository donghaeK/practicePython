'''
파이썬 실력 증진을 위한
2024 05 10 https://wikidocs.net/7014 파이썬 300문제 시작
'''

#051 리스트 생성
#2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다.
#영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
movie_rank = ["닥터 스트레인지","스플릿","럭키"]
print(movie_rank)

#052 리스트에 원소 추가
#051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append("배트맨")
print(movie_rank)

#053 movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
#"슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

#054 movie_rank 리스트에서 '럭키'를 삭제하라.
del(movie_rank[3])
print(movie_rank)

#055 movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
del(movie_rank[2:])
print(movie_rank)

