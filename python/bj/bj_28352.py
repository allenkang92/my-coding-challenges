# 문제 링크 (주석) : https://www.acmicpc.net/problem/28352
# 문제 설명:
#   N!초가 몇 주와 동일한지를 구하는 문제입니다.
#   예를 들어, 10! = 3,628,800초이고 6주도 3,628,800초이므로,
#   10!초는 6주와 같습니다.
#
# 해결 방법 설명:
#   N!을 계산한 후, 1주에 해당하는 초 수(7 * 24 * 3600)로 나눕니다.
#
# 시간/공간 복잡도 : O(N)

import sys

N = int(sys.stdin.readline().rstrip())

fac = 1
for i in range(1, N+1):
    fac *= i

# 1주 = 7일, 1일 = 24시간, 1시간 = 3600초
week = fac // (7 * 24 * 3600)
print(week)