'''
파이썬 실력 증진을 위한
2024 05 06 https://wikidocs.net/7014 파이썬 300문제 시작
'''
#1 아래 코드의 실행 결과를 예상해보세요.
a = "3"
b = "4"
print(a + b)
#답안 34(문자열이기때문에 계산이되지않는다.)

#2 아래 코드의 실행 결과를 예상해보세요.
print("Hi" * 3)
#답안 HiHiHi(문자열은 *로 반복출력가능하다.)

#3 화면에 '-'를 80개 출력하세요.
str = "-"
print(str*80)

#4 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
t1 = 'python'
t2 = 'java'
#python java python java python java python java
t3 = (t1+" "+t2+" ")*4
print(t3)

#5 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d"%(name1, age1))
print("이름: %s 나이: %d"%(name2, age2))