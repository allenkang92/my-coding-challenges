# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 간단한 문제 설명:
#   각도(angle)에 따라 예각, 직각, 둔각, 평각을 분류하여
#   예각이면 1, 직각이면 2, 둔각이면 3, 평각이면 4를 반환하는 문제.
#
# 해결 방법 설명:
#   - 0 < angle < 90이면 예각 → 1 반환
#   - angle == 90이면 직각 → 2 반환
#   - 90 < angle < 180이면 둔각 → 3 반환
#   - angle == 180이면 평각 → 4 반환
#
# 시간/공간 복잡도:
#   - 시간 복잡도: O(1) - 단일 조건 판별
#   - 공간 복잡도: O(1) - 상수 공간만 사용

def solution(angle):
    # 예각: 0 < angle < 90
    if 0 < angle < 90:
        return 1
    # 직각: angle == 90
    elif angle == 90:
        return 2
    # 둔각: 90 < angle < 180
    elif 90 < angle < 180:
        return 3
    # 평각: angle == 180
    elif angle == 180:
        return 4