# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 간단한 문제 설명 :
#   정수 배열 numbers가 매개변수로 주어질 때, 
#   numbers 원소들의 평균 값을 반환하는 문제.
#
# 해결 방법 설명 :
#   - 주어진 숫자들의 총합을 구한 후, 원소의 개수로 나누어 평균을 구함.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n) - numbers의 모든 원소에 대해 합계를 계산함.
#   - 공간 복잡도: O(1) - 추가 공간은 상수만 사용.

def solution(numbers):
    # numbers 리스트에 있는 모든 수의 합을 구하고, 
    # 리스트의 길이로 나누어 평균을 계산한다.
    answer = sum(numbers) / len(numbers)
    return answer