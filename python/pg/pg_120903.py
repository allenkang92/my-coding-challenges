# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 간단한 문제 설명 : 
#   두 배열 s1과 s2가 주어졌을 때, 두 배열에 공통으로 존재하는 원소(문자열)의 개수를 구하는 문제입니다.
#
# 해결 방법 설명 :
#   - s1 배열의 각 원소를 순회하면서 해당 원소가 s2 배열에 포함되어 있는지 확인합니다.
#   - 만약 포함되어 있다면, 동일한 원소의 개수를 세기 위해 answer를 1 증가시킵니다.
#   - 최종적으로 answer에 공통 원소의 개수를 담아 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(m * n) (m, n은 각각 s1, s2의 길이)
#   - 공간 복잡도: O(1) (추가 메모리 사용 없이 상수 공간만 사용)

def solution(s1, s2):
    answer = 0
    for element in s1:
        if element in s2:
            answer += 1
    return answer