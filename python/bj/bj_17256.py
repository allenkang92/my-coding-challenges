# 문제 링크: https://www.acmicpc.net/problem/17256
# 문제 설명:
#   마카롱이 정의한 케이크 수는 3개의 자연수 (x, y, z)로 구성된 순서쌍입니다.
#   새로운 연산 🍰는 다음과 같이 정의됩니다.
#       a 🍰 b = (a.z + b.x, a.y * b.y, a.x + b.z)
#   문제에서는 케이크 수 a와 c가 주어졌을 때, a 🍰 b = c를 만족하는 케이크 수 b를 구하는 것입니다.
#   b는 유일하게 존재함이 보장됩니다.
#
# 해결 방법:
#   각 좌표별로 등식이 성립하므로 다음과 같이 b를 구할 수 있습니다.
#       1) a.z + b.x = c.x  -->  b.x = c.x - a.z
#       2) a.y * b.y = c.y  -->  b.y = c.y // a.y (자연수이므로 정수 나눗셈 사용)
#       3) a.x + b.z = c.z  -->  b.z = c.z - a.x
#
# 시간/공간 복잡도: O(1)

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

bx = cx - az
by = cy // ay
bz = cz - ax

print(bx, by, bz)