# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181933 
# 간단한 문제 설명 : 두 정수 a, b와 boolean 변수 flag가 주어질 때,
#                  flag가 true면 a + b를, false면 a - b를 반환합니다.
# 해결 방법 설명 : flag 값에 따라 덧셈 또는 뺄셈 연산을 수행하여 결과를 반환합니다.
# 시간/공간 복잡도 : O(1) (단순 조건문과 사칙연산)

def solution(a, b, flag):
    answer = 0
    if flag == True:
        answer = a + b
    else :
        answer = a - b
    return answer