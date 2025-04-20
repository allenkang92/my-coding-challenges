# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120893
# 간단한 문제 설명 : 
#   문자열 my_string이 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 반환합니다.
#
# 해결 방법 설명 :
#   - 문자열의 각 문자를 순회하면서, 문자가 소문자이면 대문자로, 대문자이면 소문자로 변환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n)
#   - 공간 복잡도: O(n) (결과 문자열 저장)

def solution(my_string):
    answer = ''
    for i in my_string:
        if i.islower():
            answer += i.upper()
        elif i.isupper():
            answer += i.lower()
    return answer