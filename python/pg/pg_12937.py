# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12937
# 간단한 문제 설명 : 주어진 수가 짝수인지 홀수인지 판별합니다.
# 해결 방법 설명 : 2로 나눈 나머지가 0이면 짝수, 아니면 홀수입니다.
# 시간/공간 복잡도 : O(1)

def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"