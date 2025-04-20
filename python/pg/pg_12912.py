# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 간단한 문제 설명 : 두 정수 사이의 모든 정수의 합을 구합니다.
# 해결 방법 설명 : 작은 수부터 큰 수까지 순회하며 모든 수를 더합니다.
# 시간/공간 복잡도 : O(n)

def solution(a, b):
    answer = 0
    if a <= b:
        for i in range(a, b + 1):
            answer += i
    elif a > b:
        for i in range(b, a + 1):
            answer += i
    return answer