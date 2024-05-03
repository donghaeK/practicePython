'''
파이썬 실력 증진을 위한
2024 05 04 https://wikidocs.net/7014 파이썬 300문제 시작
'''
#1 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
print(letters[0],letters[2])

#2 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[4:])
#print(license_plate[-4:])

#3 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
print(string[0:5:2])

#4 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
print(string[::-1])

#5 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
phone_number = phone_number.replace('-', ' ')
print(phone_number)