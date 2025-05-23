# 문제 링크 : https://www.acmicpc.net/problem/27213
# 문제 설명:
#   Anya는 m x n 크기의 직사각형을 그리고, 그 직사각형의 테두리에 있는 모든 칸을 색칠했습니다.
#   직사각형의 테두리에 해당하는 칸의 개수를 구하는 문제입니다.
#
# 해결 방법:
#   - m과 n이 모두 1보다 큰 경우, 테두리 칸의 개수는 2*m + 2*n - 4 입니다.
#   - 만약 m 또는 n 중 하나가 1인 경우, 모든 칸이 테두리가 되므로 m * n 을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

m = int(input())
n = int(input())

if m == 1 or n == 1:
    print(m * n)
else:
    print((m + n) * 2 - 4)