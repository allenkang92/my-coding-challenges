# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/86051
# 간단한 문제 설명 : 0부터 9까지 숫자 중 numbers에 없는 숫자들의 합을 구합니다.
# 해결 방법 설명 : 0부터 9까지의 숫자를 순회하며 numbers에 없는 숫자를 찾아 더합니다.
# 시간/공간 복잡도 : O(n)

def solution(numbers):
    answer = 0
    for i in range(0, 9+1):
        if i not in numbers:
            answer += i
    return answer