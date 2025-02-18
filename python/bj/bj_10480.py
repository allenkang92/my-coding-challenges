# 문제 링크 (주석) : https://www.acmicpc.net/problem/10480
# 문제 설명:
#   입력으로 주어진 각 정수에 대해 홀수인지 짝수인지를 판별하여,
#   "x is odd" 또는 "x is even" 형태로 출력하는 문제입니다.
#
# 해결 방법 설명:
#   테스트 케이스의 수 T가 주어지고, 이후 T개의 줄마다 정수 x가 입력됩니다.
#   각 x에 대하여, x % 2 == 0 이면 짝수, 그렇지 않으면 홀수로 판단하여 출력합니다.
#
# 시간/공간 복잡도 : O(1) per 테스트 케이스

T = int(input())

for _ in range(T):
    x = int(input())
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")