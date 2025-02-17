# 문제 링크 (주석) : https://www.acmicpc.net/problem/9316
# 간단한 문제 설명:
#   주어진 N개의 테스트케이스에 대해 "Hello World, Judge i!"를 출력하는 문제입니다.
#
# 해결 방법 설명:
#   1부터 N까지 i를 순회하며, 각 줄마다 "Hello World, Judge i!"를 출력합니다.
#
# 시간/공간 복잡도 : O(N)

N = int(input())

for i in range(1, N + 1):
    print(f"Hello World, Judge {i}!")