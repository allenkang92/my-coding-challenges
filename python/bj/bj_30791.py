# 문제 링크 : https://www.acmicpc.net/problem/30791
# 간단한 문제 설명: 
#   연간 캐릭터 선거에서 경쟁률 계산하기
#   경쟁률: Tier 1(1-16위)에 속하지 않으면서, 16위 캐릭터와의 투표 차이가 1,000 이하인 캐릭터의 수
#
# 해결 방법 설명:
#   1. 입력으로 16위부터 20위까지의 투표수를 받음
#   2. 17-20위 캐릭터들 중 16위 캐릭터와의 투표수 차이가 1,000 이하인 캐릭터 수를 계산
#            
# 시간/공간 복잡도: O(1) - 고정된 수(5개)의 입력만 처리

# 입력 처리
votes = list(map(int, input().split()))

# 16위 캐릭터의 투표수
rank_16_votes = votes[0]

# 경쟁률 계산 (17위~20위 중 16위와의 차이가 1,000 이하인 캐릭터 수)
competition_rate = 0
for i in range(1, 5):  # 17위~20위 (인덱스 1~4)
    if rank_16_votes - votes[i] <= 1000:
        competition_rate += 1

# 결과 출력
print(competition_rate)