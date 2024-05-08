'''
파이썬 실력 증진을 위한
2024 05 08 https://wikidocs.net/7014 파이썬 300문제 시작
'''
#041 upper 메서드
#다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print(ticker.upper())

#042 lower 메서드
#다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "btc_krw"
print(ticker.lower())

#043 capitalize 메서드
#문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
#capitalize = 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환한다.
str = "hello"
print(str.capitalize())

#044 endswith 메서드
#파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
#endswith = 지정된 문자열로 끝나면 True, 아니면 False 반환
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx")) #True
print(file_name.endswith("xlsxx")) #False

#045 endswith 메서드
#파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
#오답1 print(file_name.endswith("xlsx,xls"))
#오답2 print(file_name.endswith(("xlsx,xls")))
#endswith 메서드는 두개이상의 문자열을 확인할때는 각각 갯수대로 호출해야한다.
print(file_name.endswith(("xlsx", "xls")))


