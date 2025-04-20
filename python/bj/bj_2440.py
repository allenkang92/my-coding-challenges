# 문제 링크 : https://www.acmicpc.net/problem/2440
# 간단한 문제 설명 : 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 출력
# 해결 방법 설명 : 0부터 N-1까지 반복하면서, (N - i)개의 별을 출력
# 시간/공간 복잡도 : O(N)

N = int(input())

for i in range(N):
    print("*" * (N - i))