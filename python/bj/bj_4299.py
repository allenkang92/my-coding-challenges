# 문제 링크 : https://www.acmicpc.net/problem/4299
# 문제 설명:
#   MK 돈스와 AFC 윔블던의 경기에서 득점한 점수의 합과 차가 주어질 때,
#   각 팀의 최종 득점을 구하는 문제입니다.
#   두 팀의 점수는 (합+차)/2와 (합-차)/2로 구할 수 있으며, 더 큰 점수를 먼저 출력합니다.
#   만약, 주어진 합과 차로 두 팀의 득점이 정수로 계산되지 않거나 음수가 된다면 -1을 출력합니다.
#
# 해결 방법 설명:
#   입력받은 합(teams_sum)과 차(teams_sub)에 대하여,
#     - teams_sum이 teams_sub보다 작거나,
#     - (teams_sum + teams_sub) 또는 (teams_sum - teams_sub)가 2로 나누어 떨어지지 않으면
#         올바른 경기 결과가 존재하지 않으므로 -1을 출력합니다.
#   그렇지 않으면,
#       team1 = (teams_sum + teams_sub) // 2
#       team2 = (teams_sum - teams_sub) // 2
#   그리고 team1, team2를 출력합니다.
#
# 시간/공간 복잡도 : O(1)

teams_sum, teams_sub = map(int, input().split())

if teams_sum < teams_sub or (teams_sum + teams_sub) % 2 != 0 or (teams_sum - teams_sub) % 2 != 0:
    print(-1)
else:
    team1 = (teams_sum + teams_sub) // 2
    team2 = (teams_sum - teams_sub) // 2
    print(team1, team2)