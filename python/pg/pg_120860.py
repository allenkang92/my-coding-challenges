# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120860
# 간단한 문제 설명 : 
#   직사각형의 네 꼭짓점 좌표가 주어질 때 넓이를 구합니다.
#
# 해결 방법 설명 : 
#   - x좌표들 중 최댓값과 최솟값의 차이로 가로 길이를 구합니다.
#   - y좌표들 중 최댓값과 최솟값의 차이로 세로 길이를 구합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

def solution(dots):
    x_coordi = [x[0] for x in dots]
    y_coordi = [y[1] for y in dots]
    width = max(x_coordi) - min(x_coordi)
    height = max(y_coordi) - min(y_coordi)
    return width * height