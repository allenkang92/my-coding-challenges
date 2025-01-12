# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120803
# 간단한 문제 설명 : 두 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 반환하는 함수를 작성하세요.
# 해결 방법 설명 : num1과 num2를 입력받아 단순히 뺄셈 연산을 수행하고 결과를 반환합니다.
# 시간/공간 복잡도 : 시간복잡도 O(1), 공간복잡도 O(1)

def solution(num1, num2):
    answer = num1 - num2
    return answer