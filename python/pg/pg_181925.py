# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181925
# 간단한 문제 설명 : numLog 배열에서 연속된 두 원소의 차이를 바탕으로 조작 문자열을 만듭니다.
#                  - 차이가 1: "w" 추가 (1 더하기)
#                  - 차이가 -1: "s" 추가 (1 빼기) 
#                  - 차이가 10: "d" 추가 (10 더하기)
#                  - 차이가 -10: "a" 추가 (10 빼기)
# 해결 방법 설명 : numLog 배열을 순회하며 인접한 두 원소의 차이를 계산하고,
#                 해당 차이에 맞는 조작 문자를 결과 문자열에 추가합니다.
# 시간/공간 복잡도 : O(n) (numLog 배열의 길이에 비례)

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