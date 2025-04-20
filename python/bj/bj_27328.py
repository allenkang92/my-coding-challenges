# 문제 링크 : https://www.acmicpc.net/problem/27328
# 간단한 문제 설명 : 두 정수 A, B를 비교하여 A < B이면 -1, A = B이면 0, A > B이면 1을 출력합니다.
# 해결 방법 설명 : if-elif-else 구문을 사용하여 A와 B의 크기를 비교하고, 조건에 따라 해당하는 값을 출력합니다.
# 시간/공간 복잡도 : O(1)

A = int(input())
B = int(input())

if A < B:
    print(-1)
elif A == B:
    print(0)
else:  # A > B
    print(1)