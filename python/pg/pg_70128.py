# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 간단한 문제 설명 : 길이가 같은 두 1차원 정수 배열 a, b의 내적을 계산합니다.
# 해결 방법 설명 : a와 b의 각 원소의 곱을 모두 더합니다.
# 시간/공간 복잡도 : O(n)

def solution(a, b):
    dot = []
    for i in range(len(a)):
        dot.append(a[i] * b[i])
    return sum(dot)