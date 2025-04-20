# 문제 링크 : https://www.acmicpc.net/problem/7595
# 문제 설명:
#   입력으로 n(1 <= n <= 100)이 주어지며, 마지막 입력은 0입니다.
#   각 n에 대해, n줄에 걸쳐 삼각형을 그리는데, 첫 줄에는 별 1개, 둘째 줄에는 별 2개, ..., n번째 줄에는 별 n개를 출력합니다.
#   삼각형들 사이에는 빈 줄이 없이 연속해서 출력합니다.
#
# 해결 방법 설명:
#   while 루프를 사용하여 n이 0이 될 때까지 입력을 받고, 각 n에 대해 1부터 n까지 반복하면서 '*'를 i번 출력합니다.
#
# 시간/공간 복잡도 : O(n) per triangle

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(1, n + 1):
        print("*" * i)