# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 간단한 문제 설명 : 주어진 정수가 양의 정수 x의 제곱인지 판별하고, 맞으면 (x+1)^2을 반환, 아니면 -1 반환
# 해결 방법 설명 : 제곱근을 구한 후 정수인지 확인
# 시간/공간 복잡도 : O(1)

def solution(n):
    sqrt_n = n ** 0.5
    if sqrt_n == int(sqrt_n):
        return (int(sqrt_n) + 1) ** 2
    return -1