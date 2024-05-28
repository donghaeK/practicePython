'''
파이썬 실력 증진을 위한
2024 05 28 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 141 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라.
# 단 부가세는 10원으로 가정한다.
# 110
# 210
# 310
xlist = [100, 200, 300]
# for i in xlist:
#     i = i[10]
#     xlist = xlist + 10
#     print(xlist)

for i in xlist:
    print(i+10)

#142 for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
ylist = ["김밥", "라면", "튀김"]
# 오늘의 메뉴: 김밥
# 오늘의 메뉴: 라면
# 오늘의 메뉴: 튀김
for i in ylist:
    print("오늘의 메뉴:",i)

#143 리스트에 주식 종목이름이 저장돼 있다.
zlist = ["SK하이닉스", "삼성전자", "LG전자"]
# 저장된 문자열의 길이를 다음과 같이 출력하라.
# 6
# 4
# 4
for i in zlist:
    print(len(i))

#144 리스트에는 동물이름이 문자열로 저장돼 있다.
alist = ['dog', 'cat', 'parrot']
#동물 이름과 글자수를 다음과 같이 출력하라.
# dog 3
# cat 3
# parrot 6
for i in alist:
    print(i,len(i))

#145 리스트에 동물 이름 저장돼 있다.
blist = ['dog', 'cat', 'parrot']
#for문을 사용해서 동물 이름의 첫 글자만 출력하라.
# d
# c
# p
for i in blist:
    print(i[0])
