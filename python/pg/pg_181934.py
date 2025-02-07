# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181934
# 간단한 문제 설명 : 두 수 n, m과 부등호(ineq)와 등호(eq)가 주어질 때, 조건에 맞으면 1, 아니면 0을 반환합니다.
# 해결 방법 설명 : 가능한 모든 부등호와 등호의 조합에 대해 조건문으로 비교 연산을 수행합니다.
# 시간/공간 복잡도 : O(1) (단순 조건문)

def solution(ineq, eq, n, m):
    answer = 0
    if ineq == ">" and eq == "=":      # '>=' 조건
        if (n >= m) == True:
            answer = 1
        else:
            answer = 0
    elif ineq == "<" and eq == "=":     # '<=' 조건
        if (n <= m) == True:
            answer = 1
        else:
            answer = 0
    elif ineq == ">" and eq == "!":     # '>' 조건   
        if (n > m) == True:
            answer = 1
        else:
            answer = 0
    elif ineq == "<" and eq == "!":     # '<' 조건
        if (n < m) == True:
            answer = 1
        else:
            answer = 0
    return answer