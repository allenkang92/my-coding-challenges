# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181925
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        if numLog[i] - numLog[i-1] == 1:
            answer += 'w'
        elif numLog[i] - numLog[i-1] == -1:
            answer += 's'
        elif numLog[i] - numLog[i-1] == 10:
            answer += 'd'
        elif numLog[i] - numLog[i-1] == -10:
            answer += 'a'
    return answer