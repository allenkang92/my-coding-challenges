# 문제 링크 (주석) : https://www.acmicpc.net/problem/30793
# 간단한 문제 설명 : 
#   선거 결과에 따른 캐릭터 타입 결정하기
#   - p_x: 예비 선거에서 캐릭터 x가 받은 투표 수
#   - r_x: 최종 선거에서 캐릭터 x가 받은 투표 수
#   - v_x = p_x / r_x (예비 선거 대 최종 선거 비율)
#   - v_x < 0.2: 캐릭터 타입 "weak"
#   - 0.2 ≤ v_x < 0.4: 캐릭터 타입 "normal"
#   - 0.4 ≤ v_x < 0.6: 캐릭터 타입 "strong"
#   - 0.6 ≤ v_x: 캐릭터 타입 "very strong"
#
# 해결 방법 설명 :
#   1. p_x와 r_x를 입력받아 v_x = p_x / r_x 계산
#   2. v_x 값을 기준으로 캐릭터 타입 결정 및 출력
#            
# 시간/공간 복잡도 : O(1) - 단순 계산 및 조건문만 사용

# 입력 처리
p_x, r_x = map(int, input().split())

# v_x 계산
v_x = p_x / r_x

# 캐릭터 타입 결정
if v_x < 0.2:
    character_type = "weak"
elif v_x < 0.4:
    character_type = "normal"
elif v_x < 0.6:
    character_type = "strong"
else:
    character_type = "very strong"

# 결과 출력
print(character_type)