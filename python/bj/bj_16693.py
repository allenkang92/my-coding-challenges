# 문제 링크 (주석) : https://www.acmicpc.net/problem/16693
# 간단한 문제 설명 : 피자 가게에서 두 가지 종류의 피자 중 어느 것이 더 가성비가 좋은지 결정하는 문제
# 해결 방법 설명 : 각 피자의 달러당 면적을 계산하여 비교
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

import math

# 입력 받기
A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())

# 가성비 계산
slice_value = A1 / P1
whole_pizza_value = (math.pi * R1 ** 2) / P2

# 결과 출력
if whole_pizza_value > slice_value:
    print('Whole pizza')
else:
    print('Slice of pizza')