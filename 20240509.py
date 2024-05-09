'''
파이썬 실력 증진을 위한
2024 05 09 https://wikidocs.net/7014 파이썬 300문제 시작
'''

#046 startswith 메서드
#파일 이름이 문자열로 저장되어 있을 때 #startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

#047 split 메서드
#다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
print(a.split(" "))
print(a.split())

#048 split 메서드
#다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
print(ticker.split("_"))

#049 split 메서드
#다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요
date = "2020-05-01"
print(date.split("-"))

#050 rstrip 메서드
#문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
data = "039490     "
print(data.rsplit())