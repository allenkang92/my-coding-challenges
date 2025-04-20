# 문제 링크 : https://www.acmicpc.net/problem/27959 
# 간단한 문제 설명 : N개의 100원 동전으로 M원 초코바를 살 수 있는지 판단하는 문제
# 해결 방법 설명 : N * 100 >= M 이면 "Yes", 아니면 "No"를 출력
# 시간/공간 복잡도 : O(1)

N, M = map(int, input().split(" "))

if N * 100 >= M:
    print("Yes")
else:
    print("No")