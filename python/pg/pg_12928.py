# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/12928#
# 간단한 문제 설명 : 주어진 숫자 n의 약수를 모두 더한 값을 반환합니다.
# 해결 방법 설명 : 1부터 n까지 순회하며 약수를 찾아 더합니다.
# 시간/공간 복잡도 : O(n)

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer