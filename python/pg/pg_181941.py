# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181941
# 간단한 문제 설명 : 문자들이 담겨있는 배열 arr의 원소들을 순서대로 이어 붙인 문자열을 반환합니다.
# 해결 방법 설명 : 파이썬의 join() 함수를 사용하여 배열의 모든 원소를 하나의 문자열로 결합합니다.
# 시간/공간 복잡도 : O(n) (배열의 길이에 비례)

def solution(arr):
    answer = ''.join(arr)
    return answer