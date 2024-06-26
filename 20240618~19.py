'''
파이썬 실력 증진을 위한
2024 06 18 ~ 19 https://wikidocs.net/7014 파이썬 300문제 시작
'''

# 241 현재시간
# datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
#
import datetime
import time

now = datetime.datetime.now()
print(now)

# 정답확인
# 242 현재시간의 타입
# datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
print(type(now))

# 243 timedelta
# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
#

for i in range(5,0,-1):
    later =datetime.timedelta(days=i)
    date = now - later
    print(date)


# 244 strftime
# 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
# 18:35:01

# 245 strptime
# datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
date = datetime.datetime.strptime("2020-05-04","%Y-%m-%d")
print(date,type(date))

# 246 sleep 함수
# time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.

# while True:
#     date = datetime.datetime.now()
#     print(date)
#     time.sleep(1)

# 247 모듈 임포트
# 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.

#import math //전체 모듈
#from math import sqrt //일부분
#import numpy as np //별칭
#from math import * //모듈의 모든 요소

# 248 os 모듈
# os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.

# import os
# print(os.getcwd())

# 249 rename 함수
# 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.
# os.rename("C:/Users/Administrator/Desktop/1.txt", "C:/Users/Administrator/Desktop/2.txt")

# 250 numpy
# numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.

import numpy as np
x = np.arange(0,5,0.1)
print(x)

for i in np.arange(0,5,0.1):
    print(i)


