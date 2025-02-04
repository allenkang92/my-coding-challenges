# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120911
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(my_string):
    answer = ''
    lower_string = sorted(my_string.lower())
    for i in lower_string:
        answer += i
    return answer