# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181934
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(ineq, eq, n, m):
    answer = 0
    if ineq == ">" and eq == "=":
        if (n >= m) == True:
            answer = 1
        else :
            answer = 0
    elif ineq == "<" and eq == "=":
        if (n <= m) == True:
            answer = 1
    elif ineq == ">" and eq == "!":    
        if (n > m) == True:
            answer = 1
        else :
            answer = 0
    elif ineq == "<" and eq == "!":
        if (n < m) == True:
            answer = 1
        else :
            answer = 0
    else :
        answer = 0
    return answer