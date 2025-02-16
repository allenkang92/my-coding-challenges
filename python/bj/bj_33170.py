# 문제 링크 (주석) : https://www.acmicpc.net/problem/33170
# 문제 설명:
#   3개의 정수 A, B, C가 주어질 때, 이들의 합이 21 이하이면 1, 초과하면 0을 출력하는 문제입니다.
#
# 해결 방법 설명:
#   A, B, C를 입력받고, 합을 계산한 뒤, 21 이하인지 판별하여 조건에 따라 1 또는 0을 출력합니다.
#
# 시간/공간 복잡도: O(1)

A = int(input())
B = int(input())
C = int(input())

if A + B + C <= 21:
    print(1)
else:
    print(0)