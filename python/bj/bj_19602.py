# 문제 링크 : https://www.acmicpc.net/problem/19602
# 문제 설명:
#   Barley 개가 하루 동안 받은 간식에 따라 행복 점수를 계산하는 문제입니다.
#   간식은 small, medium, large 세 가지 크기로 주어지며, 각 간식의 점수는 다음과 같습니다.
#       small  : 1점
#       medium : 2점
#       large  : 3점
#   Barley의 행복 점수는 1×S + 2×M + 3×L 로 계산되며,
#   점수가 10 이상이면 "happy", 그렇지 않으면 "sad"를 출력합니다.
#
# 해결 방법:
#   각 간식의 개수를 입력받은 후, 점수를 계산하고 조건에 따라 결과를 출력합니다.
#
# 시간/공간 복잡도 : O(1)

S = int(input())
M = int(input())
L = int(input())

happy_score = (S * 1) + (M * 2) + (L * 3)

if happy_score >= 10:
    print("happy")
else:
    print("sad")