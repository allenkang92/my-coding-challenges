# 문제 링크: https://www.acmicpc.net/problem/17009
# 문제 설명:
#   농구 경기에서 두 팀(애플스와 바나나스)의 득점을 기록합니다.
#   득점은 3점슛, 2점 필드골, 1점 자유투로 나오며,
#   각 팀의 득점 수치가 주어집니다.
#   애플스의 득점이 더 높으면 'A', 바나나스의 득점이 더 높으면 'B', 
#   같으면 'T'를 출력합니다.
#
# 해결 방법 설명:
#   각 팀의 총 점수는 다음과 같이 계산됩니다.
#     총점 = (3점슛 수 × 3) + (2점 필드골 수 × 2) + (1점 자유투 수 × 1)
#   계산 후 두 점수를 비교하여 결과를 출력합니다.
#
# 시간/공간 복잡도 : O(1)

A1 = int(input())
A2 = int(input())
A3 = int(input())
B1 = int(input())
B2 = int(input())
B3 = int(input())

# 올바르게 점수를 계산: A3와 B3를 이용해야 함
A_score = (A1 * 3) + (A2 * 2) + (A3 * 1)
B_score = (B1 * 3) + (B2 * 2) + (B3 * 1)

if A_score > B_score:
    print("A")
elif A_score < B_score:
    print("B")
else:
    print("T")