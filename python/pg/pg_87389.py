# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 간단한 문제 설명 : 자연수 n을 나눈 나머지가 1이 되는 가장 작은 자연수 x를 찾습니다.
# 해결 방법 설명 : 1부터 n까지 순회하며 나머지가 1이 되는 가장 작은 x를 찾습니다.
# 시간/공간 복잡도 : O(n)

def solution(n):
    answer = []
    for x in range(1, n+1):
        if n % x == 1:
            answer.append(x)
    return min(answer)