# 문제 링크 : https://www.acmicpc.net/problem/32306
# 간단한 문제 설명 : 두 팀의 농구 점수를 계산하여 승자를 결정
# 해결 방법 설명 : 각 팀의 1점, 2점, 3점 슛 성공 횟수를 입력받아 총 점수를 계산하고, 점수를 비교하여 승자를 결정
# 시간/공간 복잡도 : O(1)

# 입력 처리
team1 = list(map(int, input().split()))  # Team1의 1점, 2점, 3점 슛 성공 횟수 입력
team2 = list(map(int, input().split()))  # Team2의 1점, 2점, 3점 슛 성공 횟수 입력

# 점수 계산
score1 = team1[0] * 1 + team1[1] * 2 + team1[2] * 3  # Team1의 총 점수 계산
score2 = team2[0] * 1 + team2[1] * 2 + team2[2] * 3  # Team2의 총 점수 계산

# 승자 결정
if score1 > score2:
    print(1)  # Team1 승리
elif score2 > score1:
    print(2)  # Team2 승리
else:
    print(0)  # 동점