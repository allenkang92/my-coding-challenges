# 문제 링크 : https://www.acmicpc.net/problem/15372
# 간단한 문제 설명 : 양의 정수 N이 주어졌을 때, K가 N의 제곱의 배수인 가장 작은 양의 정수 K를 찾으세요.
# 해결 방법 설명 : K는 N²과 같거나 N²의 배수여야 합니다. 가장 작은 K는 N²입니다.
# 시간/공간 복잡도 : O(1)

import sys

# 테스트 케이스 수 입력
T = int(sys.stdin.readline().rstrip())

# 각 테스트 케이스 처리
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    K = N * N  # K는 N의 제곱
    print(K)