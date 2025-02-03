# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 간단한 문제 설명 : 
#   정수 배열 numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하는 문제.
#
# 해결 방법 설명 :
#   - 배열을 오름차순으로 정렬한 후, 가장 큰 두 원소를 선택하여 곱하면 최대값을 얻을 수 있음.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n log n) - 정렬 알고리즘 사용
#   - 공간 복잡도: O(1) (정렬 과정에서 추가 메모리 사용이 있을 수 있음)
  
def solution(numbers):
    numbers = sorted(numbers)
    answer = numbers[-1] * numbers[-2]
    return answer