# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 간단한 문제 설명 : 주어진 수 n보다 작거나 같은 가장 큰 팩토리얼 i!의 i를 찾습니다.
# 해결 방법 설명 : 1부터 시작하여 팩토리얼을 계산하고, 
#                n보다 커지면 이전 숫자를 반환합니다.
# 시간/공간 복잡도 : O(n) (n까지의 팩토리얼 계산)

def solution(n):
    factorial = 1
    i = 1
    
    while factorial <= n:
        i += 1
        factorial *= i
    
    return i - 1