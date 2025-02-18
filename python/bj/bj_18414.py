# 문제 링크 (주석) : https://www.acmicpc.net/problem/18414
# 문제 설명:
#   정수 X, L, R이 주어진다.
#   L 이상 R 이하의 정수 중에서, X와의 차의 절대값이 가장 작은 정수를 구하는 문제이다.
#   단, 그러한 정수는 유일하게 존재함이 보장된다.
#
# 해결 방법:
#   1. 먼저 X가 [L, R] 구간에 포함되면 X를 출력한다.
#   2. X가 구간에 포함되지 않으면, X보다 작은 경우에는 L, X보다 큰 경우에는 R를 출력하면 된다.
#
# 시간/공간 복잡도: O(1)

X, L, R = map(int, input().split(" "))

if L <= X <= R:
    print(X)
elif X < L:
    print(L)
else:  # X > R 인 경우
    print(R)