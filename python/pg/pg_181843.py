# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181843
# 간단한 문제 설명 : 문자열 my_string과 target이 주어질 때, target이 my_string의 부분 문자열이면 1, 아니면 0을 반환합니다.
# 해결 방법 설명 : 파이썬의 'in' 연산자를 사용해 target이 my_string 안에 존재하는지 확인합니다.
# 시간/공간 복잡도 : O(n*m) (n: my_string 길이, m: target 길이)

def solution(my_string, target):
    answer = 0
    if target in my_string:
        answer = 1
    return answer