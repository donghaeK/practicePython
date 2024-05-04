'''
파이썬 실력 증진을 위한
2024 05 05 https://wikidocs.net/7014 파이썬 300문제 시작
'''
#1 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
#실행 예 01011112222
phone_number = "010-1111-2222"
phone_number = phone_number.replace("-", "")
print(phone_number)

#2 url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
print(url[-2:])
#url = "http://sharebook.kr"
#url_split = url.split('.')
#print(url_split[-1])

#3 아래 코드의 실행 결과를 예상해보세요.
lang = 'python'
lang[0] = 'P'
print(lang)
#문자열은 immutable이기때문에 수정X
#python

#4 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
print(type(string))
string = string.replace("a", "A")
print(string)

#5 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string)
#aBcd
#변수에 따로 저장해놓은게아니라 string.replace를 그대로 호출하여 문자열이 변하지않음
