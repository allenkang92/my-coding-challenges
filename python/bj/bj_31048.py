# 문제 링크 (주석) : https://www.acmicpc.net/problem/31048
# 간단한 문제 설명 : 주어진 정수 N에 대해 N!의 마지막 자릿수를 계산
# 해결 방법 설명 : N!을 계산하고 마지막 자릿수를 출력
# 시간/공간 복잡도 : O(T * N)

import sys

# 입력 처리
input = sys.stdin.read
data = input().split()
T = int(data[0])
results = []
for i in range(1, T + 1):
    N = int(data[i])
    factorial = 1
    for j in range(1, N + 1):
        factorial *= j
    last_digit = factorial % 10
    results.append(str(last_digit))

# 결과 출력
print('\n'.join(results))