# 문제 링크 (주석) : https://www.acmicpc.net/problem/5543
# 문제 설명:
#   상근날드의 세트 메뉴 가격은 선택한 햄버거와 음료의 가격의 합에서 50원을 뺀 값입니다.
#   3종류의 햄버거와 2종류의 음료 가격이 주어질 때,
#   가장 싼 세트 메뉴 가격을 계산하여 출력하는 문제입니다.
#
# 해결 방법 설명:
#   각 햄버거와 음료의 모든 조합에 대해 세트 메뉴 가격(햄버거 가격 + 음료 가격 - 50)을 구한 뒤,
#   그 중 최솟값을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

burger1 = int(input())
burger2 = int(input())
burger3 = int(input())
beverage1 = int(input())
beverage2 = int(input())

burger_list = [burger1, burger2, burger3]
beverage_list = [beverage1, beverage2]

set_list = []

for burger in burger_list:
    for beverage in beverage_list:
        set_list.append(burger + beverage - 50)

min_set_price = min(set_list)
print(min_set_price)