'''
파이썬 실력 증진을 위한
2024 05 18 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 091 딕셔너리 생성
# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라.
# 딕셔너리의 이름은 inventory로 한다.

inventory = {"메로나": [300, 20],
             "비비빅": [400, 3],
             "죠스바": [250, 100]
             }
print(inventory)

#092 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
print(inventory["메로나"][0], "원")

#093 딕셔너리 인덱싱
#inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
print(inventory["메로나"][1], "개")

#094 딕셔너리 추가
#inventory 딕셔너리에 아래 데이터를 추가하라.
inventory["월드콘"] =[500, 7]
print(inventory)

#095 딕셔너리 keys() 메서드
#다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# iceream_key = ()
# iceream_key = icecream.keys()
iceream_key = list(icecream.keys())
print(iceream_key)
