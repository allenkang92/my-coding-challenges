# 문제 링크 : https://www.acmicpc.net/problem/2441
# 문제 설명:
#   첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는다.
#   오른쪽을 기준으로 정렬된 별을 출력하는 문제이다.
#
# 입력:
#   첫째 줄에 N (1 ≤ N ≤ 100)이 주어진다.
#
# 출력:
#   첫째 줄부터 N번째 줄까지 오른쪽 정렬된 별을 출력한다.
#
# 해결 방법:
#   각 줄마다 앞에 공백 i개, 별은 N-i개를 출력한다.
#
# 시간/공간 복잡도: O(N^2)

N = int(input())

for i in range(N):
    print((" " * i) + ("*" * (N - i)))