# 문제 링크 : https://www.acmicpc.net/problem/31090
# 문제 설명:
#   양의 정수 N이 주어졌을 때, N+1이 N의 끝 두 자리(즉, N % 100)로 나누어 떨어지는지 판별하는 문제입니다.
#   조건에 맞으면 "Good"을, 그렇지 않으면 "Bye"를 출력합니다.
#
# 해결 방법 설명:
#   연도 N의 끝 두 자리는 N % 100으로 구할 수 있습니다.
#   N+1이 이 값으로 나누어 떨어지는지 (즉, (N+1) % (N % 100) == 0 인지) 검사합니다.
#
# 시간/공간 복잡도 : O(1)

T = int(input())

for _ in range(T):
    year = int(input())
    if (year + 1) % (year % 100) == 0:
        print("Good")
    else:
        print("Bye")