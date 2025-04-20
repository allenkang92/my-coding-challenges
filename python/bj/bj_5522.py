# 문제 링크 : https://www.acmicpc.net/problem/5522
# 간단한 문제 설명 : 5번의 카드 게임 점수를 입력받아 총점을 계산하는 프로그램
# 해결 방법 설명 : for 루프를 사용하여 5번의 점수를 입력받고, total_score 변수에 누적하여 합산
# 시간/공간 복잡도 : O(1) (고정된 횟수의 입력 및 연산)

total_score = 0

for _ in range(5):
    A = int(input())
    total_score += A

print(total_score)