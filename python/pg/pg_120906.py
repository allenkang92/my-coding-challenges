# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 간단한 문제 설명 :
#   정수 n이 주어질 때, n의 각 자리 숫자의 합을 계산하여 반환합니다.
#
# 해결 방법 설명 :
#   - n을 문자열로 변환한 후, 각 자리 숫자를 정수로 변환하여 합산합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(d) - n의 자리수 d에 따라 계산
#   - 공간 복잡도: O(d) - 문자열 변환 및 리스트 사용

def solution(n):
    answer = []
    n = str(n)
    for digit in n:
        answer.append(int(digit))
    return sum(answer)