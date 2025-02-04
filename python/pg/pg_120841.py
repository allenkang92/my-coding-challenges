# 문제 설명:
#   x 좌표와 y 좌표가 주어진 점 dot이 어느 사분면에 속하는지 구하는 문제입니다.
#
# 해결 방법 설명:
#   - 점의 좌표를 확인하여:
#       - x > 0, y > 0: 제1사분면 (return 1)
#       - x < 0, y > 0: 제2사분면 (return 2)
#       - x < 0, y < 0: 제3사분면 (return 3)
#       - x > 0, y < 0: 제4사분면 (return 4)
#
# 시간/공간 복잡도:
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    elif dot[0] > 0 and dot[1] < 0:
        return 4