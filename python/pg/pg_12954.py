# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12954
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 
def solution(x, n):
    answer = []
    if x == 0:
        answer = [0] * n
    elif x > 0:
        for i in range(x, x * (n + 1), x):
            answer.append(i)
    else:
        for i in range(x, x * (n + 1), x):
            answer.append(i)
    return answer