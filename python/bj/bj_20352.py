# 문제 링크 : https://www.acmicpc.net/problem/20353
# 문제 설명:
#   원형 텐트의 면적 a가 주어지면, 텐트를 완전히 둘러싸는 원형 담장(울타리)의 총 길이를 구하는 문제입니다.
#   원의 면적이 a이므로, 반지름 r은 r = √(a/π) 로 계산할 수 있고,
#   원의 둘레는 2 × π × r 입니다.
#   따라서 최종적으로 구해야 할 울타리의 길이는 2 × π × √(a/π) = 2 × √(a×π) 입니다.
#
# 해결 방법:
#   math 모듈의 sqrt()와 pi 상수를 이용하여 2 * sqrt(a * pi)를 계산한 후 출력합니다.
#
# 시간/공간 복잡도 : O(1)

import math

a = int(input())
fence_length = 2 * math.sqrt(a * math.pi)
print(fence_length)