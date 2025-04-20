# 문제 링크 : https://www.acmicpc.net/problem/8558
# 간단한 문제 설명 : 주어진 n에 대해 n!의 일의 자리 숫자를 계산하는 프로그램입니다.
# 해결 방법 설명 : n이 5 이상이면 0을 출력하고, 그렇지 않으면 n!을 계산하여 일의 자리 숫자를 출력합니다.
# 시간/공간 복잡도 : O(n)

n = int(input())

if n == 0 or n == 1:
    print(1)
elif n >= 5:
    print(0)
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial % 10)