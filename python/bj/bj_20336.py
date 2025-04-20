# 문제 링크 : https://www.acmicpc.net/problem/20336
# 간단한 문제 설명 : 여러 세트 메뉴 중 하나를 무작위로 선택하여 추천 메뉴를 출력하는 문제
# 해결 방법 설명 : 무작위로 하나의 세트 메뉴를 선택하고, 해당 메뉴의 요리 목록을 출력
# 시간/공간 복잡도 : O(n) (세트 메뉴 개수에 비례하는 시간과 공간이 소요됨)

import random

# 입력 받기
n = int(input())  # 세트 메뉴의 개수
menus = []  # 세트 메뉴 목록

for _ in range(n):
    menu = input().split()  # 메뉴 입력 (첫 번째 값은 요리 개수)
    menus.append(menu[1:])  # 요리 목록만 저장

# 무작위로 하나의 메뉴 선택
selected_menu = random.choice(menus)

# 결과 출력
print(len(selected_menu))  # 추천할 요리의 개수
for dish in selected_menu:
    print(dish)  # 추천할 요리 목록