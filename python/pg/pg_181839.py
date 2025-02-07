# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181839
# 간단한 문제 설명 : 두 주사위의 숫자 a, b가 주어질 때 다음 규칙에 따라 점수를 계산합니다.
#                  - 둘 다 홀수: a^2 + b^2
#                  - 하나만 홀수: 2 * (a + b)
#                  - 둘 다 짝수: |a - b|
# 해결 방법 설명 : a와 b의 홀짝 여부를 확인하고 규칙에 따라 점수를 계산합니다.
# 시간/공간 복잡도 : O(1) (상수 시간)

def solution(a, b):
    answer = 0
    if a % 2 != 0 and b % 2 != 0:      # 둘 다 홀수인 경우
        answer += a ** 2 + b ** 2
    elif a % 2 == 0 and b % 2 == 0:     # 둘 다 짝수인 경우
        answer += abs(a - b)
    else:                               # 하나만 홀수인 경우
        answer += 2 * (a + b)
    return answer