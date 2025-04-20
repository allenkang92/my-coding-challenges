# 문제 링크 : https://www.acmicpc.net/problem/27434
# 간단한 문제 설명 : 0보다 크거나 같은 정수 N이 주어졌을 때, N!을 출력하는 프로그램을 작성하시오. (0 ≤ N ≤ 100,000)
# 해결 방법 설명 : 반복문을 사용하여 1부터 N까지의 모든 정수를 곱합니다. N이 0일 경우 팩토리얼은 1입니다.
# 시간/공간 복잡도 : O(N)

import sys

N = int(sys.stdin.readline())

fac = 1
for i in range(1, N+1):
    fac *= i

if N == 0:
    fac = 1
print(fac)