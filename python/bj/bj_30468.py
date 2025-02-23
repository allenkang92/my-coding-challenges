# 문제 링크 (주석) : https://www.acmicpc.net/problem/30468
# 문제 설명:
#   호반우의 현재 스탯인 힘(STR), 민첩(DEX), 지능(INT), 운(LUK)과 목표 평균 스탯 수치 N이 주어진다.
#   각 스탯은 축복을 사용하여 1씩 올릴 수 있으며, 
#   축복을 최소 몇 번 사용해야 호반우의 평균 스탯 수치가 N 이상이 되는지 구하는 문제이다.
#
#   평균 스탯 수치는 (STR + DEX + INT + LUK) / 4 로 계산된다.
#
# 입력:
#   첫 번째 줄에 STR, DEX, INT, LUK와 N이 공백으로 구분되어 주어진다. 
#   (1 ≤ STR, DEX, INT, LUK, N ≤ 100)
#
# 출력:
#   호반우의 평균 스탯 수치를 N 이상으로 만들기 위해 사용해야 할 축복의 최소 횟수를 출력한다.
#
# 해결 방법:
#   현재 스탯의 총합을 sum이라 하고, 목표 총합은 4 * N이다.
#   따라서 필요한 축복의 횟수는 max(0, 4 * N - sum)으로 구할 수 있다.
#
# 시간/공간 복잡도: O(1)

STR, DEX, INT, LUK, N = map(int, input().split())
stat_sum = STR + DEX + INT + LUK
needed_blessings = max(0, 4 * N - stat_sum)
print(needed_blessings)