# 문제 링크 (주석) : https://www.acmicpc.net/problem/4562
# 간단한 문제 설명 : 좀비가 먹은 뇌(A)와 필요한 뇌(B)를 비교하여 A >= B이면 "MMM BRAINS", 아니면 "NO BRAINS" 출력
# 시간/공간 복잡도 : O(n)

n = int(input())

for _ in range(n):
    A, B = map(int, input().split())
    if A < B:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")