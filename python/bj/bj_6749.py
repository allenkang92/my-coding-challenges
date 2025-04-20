# 문제 링크 : https://www.acmicpc.net/problem/6749
# 문제 설명:
#   세 자녀의 나이는 등차수열을 이룹니다.
#   주어진 Y(막내 아이의 나이)와 M(둘째 아이의 나이)을 이용해,
#   셋째 아이(막내가 아니라 가장 나이가 많은 아이)의 나이를 구합니다.
#   등차가 (M - Y) 이므로, 가장 큰 나이는 M + (M - Y) 입니다.
#
# 해결 방법 설명:
#   diff = M - Y
#   oldest = M + diff
#
# 시간/공간 복잡도 : O(1)

Y = int(input())
M = int(input())

diff = M - Y

print(M + diff)