# 문제 링크 (주석) : https://www.acmicpc.net/problem/3733
# 간단한 문제 설명 : N명의 사람과 ACM 심판위원장이 S개의 주식을 똑같이 나눌 때, 각 사람이 가질 수 있는 최대 주식 수 x를 구하는 프로그램
# 해결 방법 설명 : 각 사람이 가질 수 있는 최대 주식 수는 S / (N + 1)의 몫
# 시간/공간 복잡도 : O(1)

while True:
    try:
        N, S = map(int, input().split())
        print(S // (N + 1))
    except EOFError:
        break