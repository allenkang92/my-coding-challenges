# 문제 링크 (주석) : https://www.acmicpc.net/problem/33046
# 간단한 문제 설명 : 
#   마작 게임에서 두 개의 주사위를 두 번 굴려 누가 진동(게임 시작 플레이어)이 되는지 결정
#   좌동(1번 플레이어)이 첫 주사위를 굴리고, 그 합이 가리키는 사람이 가동이 됨
#   가동이 두 번째 주사위를 굴리고, 그 합이 가리키는 사람이 진동이 됨
#   주사위 합이 가리키는 사람은 주사위를 굴린 사람부터 반시계방향으로 그 합만큼 세어나감
# 
# 해결 방법 설명 :            
#   1. 첫 주사위 합에서 가동 결정: (first_sum - 1) % 4 + 1
#      - 주사위를 굴린 사람(좌동=1번)부터 first_sum명을 세어 결정
#   2. 두 번째 주사위 합에서 진동 결정: (gadong + second_sum - 2) % 4 + 1
#      - 주사위를 굴린 사람(가동)부터 second_sum명을 세어 결정
# 
# 시간/공간 복잡도 : O(1) - 단순 계산만 수행

# 입력 처리
A, B = map(int, input().split())
C, D = map(int, input().split())

# 주사위 합 계산
first_sum = A + B
second_sum = C + D

# 가동 결정 (좌동은 1번 플레이어)
# 좌동(1번)으로부터 first_sum명을 세어 결정
gadong = (first_sum - 1) % 4 + 1

# 진동 결정
# 가동으로부터 second_sum명을 세어 결정
jindong = (gadong + second_sum - 2) % 4 + 1

# 결과 출력
print(jindong)