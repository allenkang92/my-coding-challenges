# 문제 링크 (주석) : https://www.acmicpc.net/problem/28248
# 간단한 문제 설명 : Deliv-e-droid 게임에서 최종 점수를 계산
# 해결 방법 설명 : 배달한 패키지 수와 충돌 횟수를 기반으로 점수를 계산하고, 보너스 점수를 추가
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 받기
P = int(input())
C = int(input())

# 점수 계산
score = P * 50 - C * 10
if P > C:
    score += 500

# 결과 출력
print(score)