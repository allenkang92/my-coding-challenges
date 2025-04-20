# 문제 링크 : https://www.acmicpc.net/problem/18198
# 간단한 문제 설명 : Alice와 Barbara의 농구 게임 기록을 바탕으로 승자를 결정하는 문제
# 해결 방법 설명 : 기록을 순회하며 점수를 계산하고, 11점 이상 달성 및 2점 차이로 앞서는 경우 승자를 결정
# 시간/공간 복잡도 : O(n) (기록 길이에 비례하는 시간과 공간이 소요됨)

# 입력 받기
record = input().strip()  # 게임 기록

# 점수 초기화
alice_score = 0
barbara_score = 0

# 기록 순회하며 점수 계산
for i in range(0, len(record), 2):
    player = record[i]  # 플레이어 (A 또는 B)
    points = int(record[i + 1])  # 점수 (1 또는 2)
    
    if player == 'A':
        alice_score += points
    else:
        barbara_score += points
    
    # 승자 결정 조건 확인
    if alice_score >= 11 and alice_score >= barbara_score + 2:
        print('A')
        break
    if barbara_score >= 11 and barbara_score >= alice_score + 2:
        print('B')
        break