# 문제 링크 (주석) : https://www.acmicpc.net/problem/27855
# 간단한 문제 설명 : Cornhole 게임에서 두 플레이어의 점수를 계산하고, 점수 차이에 따라 승자를 결정
# 해결 방법 설명 : 각 플레이어의 점수를 계산하고, 점수 차이를 바탕으로 승자를 결정
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 처리
H1, B1 = map(int, input().split())
H2, B2 = map(int, input().split())

# 점수 계산
score1 = H1 * 3 + B1
score2 = H2 * 3 + B2

# 결과 출력
if score1 == score2:
    print("NO SCORE")
else:
    if score1 > score2:
        print(1, score1 - score2)
    else:
        print(2, score2 - score1)