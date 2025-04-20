# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120851
# 간단한 문제 설명:
#   문자열 my_string 안의 모든 한 자리 자연수들의 합을 return합니다.
#
# 해결 방법 설명:
#   - 문자열의 각 문자를 순회하며, 해당 문자가 숫자인지 확인합니다.
#   - 숫자인 경우 int()로 변환한 뒤 결과에 더합니다.
#
# 시간/공간 복잡도:
#   - 시간 복잡도: O(n)
#   - 공간 복잡도: O(1)

def solution(my_string):
    answer = 0
    for ch in my_string:
        if ch.isdigit():
            answer += int(ch)
    return answer