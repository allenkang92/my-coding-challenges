# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 간단한 문제 설명 : 
#   정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 반환합니다.
#
# 해결 방법 설명 : 
#   - 배열에서 최대값을 max() 함수를 통해 구합니다.
#   - 최대값의 인덱스는 index() 함수를 통해 구합니다.
#   - 두 값을 배열에 담아 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n)
#   - 공간 복잡도: O(1)

def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer