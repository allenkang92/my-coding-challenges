# 문제 링크 (주석) : https://www.acmicpc.net/problem/30794
# 간단한 문제 설명 : 
#   클럽 오디션 게임에서 키 노트의 레벨(lv)과 판정에 따라 획득 점수를 계산하는 문제
#   - miss: 0점
#   - bad: 200 × lv 점
#   - cool: 400 × lv 점
#   - great: 600 × lv 점
#   - perfect: 1000 × lv 점 (여기서는 1연팩 가정)
#
# 해결 방법 설명 : 
#   레벨과 판정 정보를 입력받아 판정에 따른 점수 공식에 맞게 계산한다.
#   perfect의 경우, 문제 조건에 따라 1연팩으로 계산한다.
#            
# 시간/공간 복잡도 : O(1) - 단순 조건 판단 및 계산

# 입력 처리
lv, judgment = input().split()
lv = int(lv)

# 판정에 따른 점수 계산
if judgment == "miss":
    score = 0
elif judgment == "bad":
    score = 200 * lv
elif judgment == "cool":
    score = 400 * lv
elif judgment == "great":
    score = 600 * lv
elif judgment == "perfect":
    score = 1000 * lv  # 1연팩 가정

# 결과 출력
print(score)