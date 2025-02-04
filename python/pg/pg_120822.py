# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120822
# 간단한 문제 설명 : 
#   문자열 my_string이 주어질 때, 이를 거꾸로 뒤집은 문자열을 반환합니다.
#
# 해결 방법 설명 : 
#   - 슬라이싱(my_string[::-1])을 사용하여 문자열을 뒤집습니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n)
#   - 공간 복잡도: O(n)

def solution(my_string):
    return my_string[::-1]