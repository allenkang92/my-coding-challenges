# 문제 링크 (주석) : https://www.acmicpc.net/problem/26566
# 간단한 문제 설명:
#   피자를 두 가지 방식으로 구매할 수 있다:
#   1. 피자 조각: 면적 A1, 가격 P1
#   2. 원형 피자: 반지름 R1, 가격 P2
#   달러당 더 많은 피자를 얻을 수 있는 방법(조각 또는 전체 피자)을 선택해야 한다.
#
# 해결 방법 설명:
#   각 옵션에서 달러당 얻을 수 있는 피자의 양을 계산한다:
#   - 피자 조각: A1/P1 (면적/가격)
#   - 원형 피자: πR1^2/P2 (면적/가격)
#   더 큰 값을 가진 옵션을 선택한다.
#            
# 시간/공간 복잡도: O(n), n은 테스트 케이스의 수

from math import pi

n = int(input())
for _ in range(n):
    A1, P1 = map(int, input().split(" "))
    R1, P2 = map(int, input().split(" "))
    P1_agg = (A1 / P1)
    P2_agg = ((pi * (R1 ** 2)) / P2)
    if P1_agg >= P2_agg:
        print("Slice of pizza")
    else: 
        print("Whole pizza")