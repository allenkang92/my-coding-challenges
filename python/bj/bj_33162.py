# 문제 링크 : https://www.acmicpc.net/problem/33162
# 간단한 문제 설명 : 
#   JOI는 일직선 도로에서 산책을 하고 있음
#   다음 행동을 교대로 반복:
#   - 행동 A: 3m 전진
#   - 행동 B: 2m 후퇴
#   총 X번의 행동 후 처음 위치에서 얼마나 앞으로 이동했는지 계산하는 문제
# 
# 해결 방법 설명 :            
#   1. 홀수 번째 행동은 항상 A (3m 전진)
#   2. 짝수 번째 행동은 항상 B (2m 후퇴)
#   3. 행동 A의 횟수와 행동 B의 횟수를 계산하여 총 이동 거리 구함
# 
# 시간/공간 복잡도 : O(1) - 단순 계산만 수행

# 입력 처리
X = int(input())

# 행동 A와 행동 B의 횟수 계산
action_A_count = (X + 1) // 2  # 홀수 번째 행동 (올림 나눗셈)
action_B_count = X // 2        # 짝수 번째 행동 (내림 나눗셈)

# 총 이동 거리 계산
total_distance = (action_A_count * 3) - (action_B_count * 2)

# 결과 출력
print(total_distance)