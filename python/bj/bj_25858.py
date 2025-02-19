# 문제 링크 (주석) : https://www.acmicpc.net/problem/25858
# 문제 설명:
#   여름 동안 팀원들이 푼 문제 수에 따라 상금(d 달러)을 분배하는 문제입니다.
#   첫 번째 입력 줄에는 팀원의 수 n과 나눌 총 상금 d가 주어집니다.
#   이후 n개의 줄에 걸쳐 각 팀원이 푼 문제의 수가 주어집니다.
#   한 문제당 상금은 전체 상금 d를 모든 팀원이 푼 문제 수의 합으로 나눈 값입니다.
#   입력 조건에 따라 한 문제당 상금은 정수입니다.
#   각 팀원의 상금은 (해당 팀원이 푼 문제 수) × (문제당 상금) 입니다.
#
# 해결 방법:
#   각 팀원이 푼 문제 수의 총합을 구한 후, 상금을 문제 수의 총합으로 나누어 한 문제당 상금을 구합니다.
#   그리고 각 팀원의 상금을 계산하여 출력합니다.
#
# 시간/공간 복잡도 : O(n)

n, d = map(int, input().split(" "))
solved_list = []
for _ in range(n):
    solved_list.append(int(input()))
total_solved = sum(solved_list)
per_problem = d // total_solved  # 한 문제당 상금 (정수임이 보장됨)

for solved in solved_list:
    print(solved * per_problem)