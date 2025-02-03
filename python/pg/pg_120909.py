# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 간단한 문제 설명 : 
#   정수 n이 주어질 때, n이 제곱수라면 1을, 아니라면 2를 반환하는 문제입니다.
#
# 해결 방법 설명 :
#   - n의 제곱근을 계산합니다.
#   - 제곱근이 정수이면 n은 제곱수이므로 1을 반환하고,
#     그렇지 않으면 2를 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

def solution(n):
    sqrt_n = n ** 0.5  # n의 제곱근 계산
    # 제곱근이 정수인지 판별
    if sqrt_n == int(sqrt_n):
        return 1
    else:
        return 2