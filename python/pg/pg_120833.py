# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120833
# 간단한 문제 설명 : 
#   정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, 
#   numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 합니다.
#
# 해결 방법 설명 :
#   - 슬라이싱을 사용하여 num1번 인덱스부터 num2번 인덱스까지 자른 배열을 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n) (슬라이싱 연산)
#   - 공간 복잡도: O(n) (결과 배열 저장)

def solution(numbers, num1, num2):
    answer = numbers[num1:num2+1]
    return answer