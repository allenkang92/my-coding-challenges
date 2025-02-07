# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181930
# 간단한 문제 설명 : 세 개의 주사위 숫자 a, b, c가 주어질 때, 다음 규칙에 따라 점수를 계산합니다.
#                  - 모두 다르면: a + b + c
#                  - 두 숫자만 같으면: (a+b+c) × (a^2 + b^2 + c^2)
#                  - 모두 같으면: (a+b+c) × (a^2 + b^2 + c^2) × (a^3 + b^3 + c^3)
# 해결 방법 설명 : 세 숫자의 동일 여부를 확인하여 각 경우에 맞는 계산식을 적용합니다.
# 시간/공간 복잡도 : O(1) (단순 비교 및 계산)

def solution(a, b, c):
    answer = 0
    if a == b == c:  # 세 숫자가 모두 같은 경우
        answer += (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif (a == b and a != c) or (a == c and a != b) or (b == c and a != b):  # 두 숫자만 같은 경우
        answer += (a+b+c) * (a**2 + b**2 + c**2)
    elif a != b and b != c and c != a:  # 세 숫자가 모두 다른 경우
        answer += a + b + c
    return answer