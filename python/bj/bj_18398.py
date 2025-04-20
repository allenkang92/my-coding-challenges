# 문제 링크 : https://www.acmicpc.net/problem/18398
# 문제 설명:
#   아프가니스탄의 한 도시에서 두 자매가 수학 숙제를 도와줄 간단한 게임을 만들려고 합니다.
#   숙제는 두 정수의 합과 곱을 계산하는 문제입니다.
#
# 해결 방법 설명:
#   첫째 줄에 테스트 케이스의 수 T가 주어집니다.
#   각 테스트 케이스마다 먼저 문제의 개수 N이 주어지고, 이후 N개의 줄에 두 정수 Ai와 Bi가 주어집니다.
#   각 문제마다 두 수의 합과 곱을 한 줄에 출력합니다.
#
# 시간/공간 복잡도 : O(T * N)

T = int(input())
for _ in range(T):
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        print(a + b, a * b)