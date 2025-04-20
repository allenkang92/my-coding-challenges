# 문제 링크 : https://www.acmicpc.net/problem/30007
# 간단한 문제 설명 : 라면 공식에 따라 필요한 물의 양을 계산하는 문제
# 해결 방법 설명 : 라면 공식 W = A * (X - 1) + B를 사용하여 필요한 물의 양을 계산
# 시간/공간 복잡도 : O(N)

N = int(input())

for _ in range(N):
    A, B, X = map(int, input().split(" "))
    W = (A * (X - 1)) + B
    print(W)