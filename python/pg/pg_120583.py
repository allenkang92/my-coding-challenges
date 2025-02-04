# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120583
# 간단한 문제 설명 : 
#   정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는지를 반환합니다.
#
# 해결 방법 설명 :
#   - 배열 array의 각 원소를 순회하며, 원소가 n과 같으면 카운트를 1 증가시킵니다.
#   - 최종 카운트를 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(m) (m은 array의 길이)
#   - 공간 복잡도: O(1) (추가 메모리 사용 없음)

def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer