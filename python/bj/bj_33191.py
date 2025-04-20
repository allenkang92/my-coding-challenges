# 문제 링크 : https://www.acmicpc.net/problem/33191
# 간단한 문제 설명 : 
#   Mahya는 Yalda 축제를 위해 하나의 전통 아이템을 구매하려 함
#   제한된 예산(b)으로 선호도 순서대로 아이템을 선택해야 함
#   선호도 순서: 수박(Watermelon) > 석류(Pomegranates) > 견과류(Nuts)
#   예산이 부족하면 아무것도 구매하지 못함
#
# 해결 방법 설명 :            
#   1. Mahya의 예산과 각 아이템의 가격을 입력받음
#   2. 선호도 순서대로 예산으로 구매 가능한지 확인
#   3. 가능한 가장 선호하는 아이템을 출력, 모두 불가능하면 "Nothing" 출력
#
# 시간/공간 복잡도 : O(1) - 단순 조건 체크만 수행

# Mahya의 예산 입력
b = int(input())

# 각 아이템의 가격 입력
watermelon_price = int(input())
pomegranates_price = int(input())
nuts_price = int(input())

# 예산으로 살 수 있는 가장 선호하는 아이템 결정
if b >= watermelon_price:
    print("Watermelon")
elif b >= pomegranates_price:
    print("Pomegranates")
elif b >= nuts_price:
    print("Nuts")
else:
    print("Nothing")