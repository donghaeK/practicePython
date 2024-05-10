'''
파이썬 실력 증진을 위한
2024 05 11 https://wikidocs.net/7014 파이썬 300문제 시작
'''

#056 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

#057 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print("max: ",max(nums))
print("min: ",min(nums))

#058 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#059 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#060 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

