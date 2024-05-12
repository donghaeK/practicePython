'''
파이썬 실력 증진을 위한
2024 05 13 https://wikidocs.net/7014 파이썬 300문제 시작
'''

#066 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
#출력 예시: 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print(interest[0],interest[1],interest[2],interest[3],interest[4])
interest2 = " ".join(interest)
print(interest2)

#067 join 메서드
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시: 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
interest = "/".join(interest)
print(interest)

#068 join 메서드
#출력 예시:
#삼성전자
#LG전자
#Naver
#SK하이닉스
#미래에셋대우
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
interest = "\n".join(interest)
print(interest)

#069 문자열 split 메서드
#회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
string = "삼성전자/LG전자/Naver"
#이를 interest 이름의 리스트로 분리 저장하라.
#실행 예시
#>> print(interest)
#['삼성전자', 'LG전자', 'Naver']
interest = string.split("/")
print(interest)

#070 리스트 정렬
#리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)