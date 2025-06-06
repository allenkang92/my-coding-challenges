# 문제 링크 : https://www.acmicpc.net/problem/16428
# 간단한 문제 설명 : 두 정수 A와 B가 주어질 때, 수학적 정의에 맞는 몫과 나머지를 구하는 문제
# 해결 방법 설명 : 파이썬의 기본 나눗셈 연산자는 음수 처리가 다르므로 수학적 정의(A = qB + r, 0 ≤ r < |B|)에 맞게 계산
# 시간/공간 복잡도 : O(1), 단순 연산만 수행

import sys
input = sys.stdin.readline

# 두 정수 A, B 입력
A, B = map(int, input().split())

# 몫 계산
if A * B >= 0:  # A와 B의 부호가 같거나 A가 0인 경우
    q = A // B
else:  # A와 B의 부호가 다른 경우
    q = -(abs(A) // abs(B))
    if A % B != 0:  # 나누어 떨어지지 않으면 몫을 1 더 내림
        q -= 1

# 나머지 계산 (A = qB + r 관계 이용)
r = A - q * B

# 결과 출력
print(q)
print(r)