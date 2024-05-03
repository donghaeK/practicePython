'''
파이썬 실력 증진을 위한
2024 05 03 https://wikidocs.net/7014 파이썬 300문제 시작
'''
#1 문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
print(int(num_str)); print(type(int(num_str)))

#2 정수 100을 문자열 '100'으로 변환해보세요.
num = 100
num = "100"
print(num); print(type(num))

num = 100
result = str(num)
print(result, type(result))

#3 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
s = "15.79"
print(float(s))

#4 year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다.
# 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
year = int(year)
for i in range(3):
    year = year + 1
    print(year)

#5 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.
# 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
ac_1m = 48584
ac_36m = ac_1m * 36
print(ac_36m)