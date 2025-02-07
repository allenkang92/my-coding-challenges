# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181926
# 간단한 문제 설명 : 정수 n과 문자열 control이 주어질 때, control의 각 문자에 따라 n을 조작한 최종 값을 반환합니다.
#                  - "w": n이 1 증가
#                  - "s": n이 1 감소 
#                  - "d": n이 10 증가
#                  - "a": n이 10 감소
# 해결 방법 설명 : control 문자열의 각 문자를 순회하며 해당하는 연산을 n에 적용합니다.
# 시간/공간 복잡도 : O(n) (control 문자열의 길이에 비례)

def solution(n, control):
    answer = n
    for ch in control:
        if ch == "w":
            answer += 1
        elif ch == "s":
            answer -= 1
        elif ch == "d":
            answer += 10
        elif ch == "a":    
            answer -= 10
    return answer