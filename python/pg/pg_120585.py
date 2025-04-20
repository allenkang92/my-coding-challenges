# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 간단한 문제 설명 : 
#   머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 주어질 때,
#   머쓱이보다 키 큰 사람의 수를 반환하는 문제입니다.
#
# 해결 방법 설명 : 
#   - 배열의 각 원소를 확인하여 머쓱이의 키보다 큰 경우 answer를 1 증가시킵니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(n) - 배열의 모든 원소를 한 번씩 확인
#   - 공간 복잡도: O(1) - 상수 공간 사용

def solution(array, height):
    answer = 0
    for person in array:
        if person > height:
            answer += 1
    return answer