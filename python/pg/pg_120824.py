# 문제 링크 : (문제 링크 생략)
# 간단한 문제 설명 :
#   정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 반환합니다.
#
# 해결 방법 설명 :
#   - 리스트의 각 원소를 순회하며, 짝수인 경우와 홀수인 경우를 구분하여 각각 카운트합니다.
#   - 카운트한 짝수와 홀수의 개수를 차례대로 배열에 저장하여 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n)
#   - 공간 복잡도: O(1) (결과 배열의 크기는 상수)

def solution(num_list):
    answer = []
    odds = 0
    evens = 0
    for i in num_list:
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    answer.append(evens)
    answer.append(odds)
    return answer