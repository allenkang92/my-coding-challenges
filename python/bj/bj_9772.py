# 문제 링크 (주석) : https://www.acmicpc.net/problem/9772
# 문제 설명:
#   2차원 평면 상의 점 좌표 (x, y)가 주어질 때, 해당 점이 어느 사분면에 위치하는지 출력하는 문제입니다.
#   단, 좌표 중 하나라도 0이면 해당 점은 축 위에 있는 것으로 간주하여 "AXIS"를 출력합니다.
#   입력의 마지막 줄은 "0 0"으로 주어지며, 이는 출력한 후 프로그램을 종료합니다.
#
# 해결 방법 설명:
#   각 점의 좌표를 입력받아,
#     - x와 y 모두 0이면 "AXIS"를 출력하고 종료합니다.
#     - x 또는 y가 0이면 "AXIS"를 출력합니다.
#     - x > 0, y > 0이면 Q1,
#     - x < 0, y > 0이면 Q2,
#     - x < 0, y < 0이면 Q3,
#     - x > 0, y < 0이면 Q4를 출력합니다.
#
# 시간/공간 복잡도 : O(1) per 입력

while True:
    x, y = map(float, input().split())
    if x == 0 and y == 0:
        print("AXIS")
        break
    elif x == 0 or y == 0:
        print("AXIS")
    elif x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif x > 0 and y < 0:
        print("Q4")