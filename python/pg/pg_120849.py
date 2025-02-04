# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 간단한 문제 설명 : 
#   문자열 my_string이 주어질 때, 모음(a, e, i, o, u)을 제거한 문자열을 반환하는 문제입니다.
#
# 해결 방법 설명 :
#   - 모음을 저장한 리스트 or 문자열 vowels를 사용하여 각 문자가 모음이 아닌 경우에만 answer에 추가합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n) - my_string의 모든 문자에 대해 검사
#   - 공간 복잡도: O(n) - answer에 새로운 문자열 생성

def solution(my_string):
    answer = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in my_string:
        if char not in vowels:
            answer += char
    return answer