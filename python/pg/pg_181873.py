# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181873
# 간단한 문제 설명 : 영소문자로 이루어진 문자열 my_string에서 alp에 해당하는 모든 글자를 대문자로 변환하여 반환합니다.
# 해결 방법 설명 : 문자열의 replace() 메서드를 사용하여 my_string 내의 alp를 alp.upper()로 치환합니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

def solution(my_string, alp):
    answer = my_string.replace(alp, alp.upper())
    return answer