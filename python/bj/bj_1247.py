# 문제 링크 : https://www.acmicpc.net/problem/1247
# 문제 설명:
#   N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 문제이다.
#
# 입력:
#   총 3개의 테스트 셋이 주어진다.
#   각 테스트 셋의 첫째 줄에는 N (1 ≤ N ≤ 100,000)이 주어지고,
#   둘째 줄부터 N개의 줄에 걸쳐 각 정수가 주어진다.
#   주어지는 정수의 절댓값은 9,223,372,036,854,775,807보다 작거나 같다.
#
# 출력:
#   각 테스트 셋에 대해 N개의 정수들의 합 S의 부호를 출력한다.
#   S가 0이면 "0"을, S가 양수이면 "+"를, 음수이면 "-"를 출력한다.
#
# 시간/공간 복잡도: O(N) per test set

for _ in range(3):
    N = int(input())
    total = 0
    for _ in range(N):
        total += int(input())
    if total == 0:
        print("0")
    elif total > 0:
        print("+")
    else:
        print("-")