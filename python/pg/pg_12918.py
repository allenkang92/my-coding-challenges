# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 간단한 문제 설명 : 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼 있는지 확인하는 함수, solution을 완성합니다.
# 해결 방법 설명 : 문자열 s의 길이가 4 혹은 6인지 확인하고, s.isdigit()을 사용하여 숫자로만 이루어졌는지 확인합니다.
# 시간/공간 복잡도 : O(1)

def solution(s):
    answer = True
    if (len(s) == 4 or len(s) == 6 ) and s.isdigit() == True:
        answer = True
    else :
        answer = False
    return answer