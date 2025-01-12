# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120805
# 간단한 문제 설명 : 정수 num1과 num2가 주어질 때, num1을 num2로 나눈 몫을 반환하는 함수를 작성하세요.
# 해결 방법 설명 : num1과 num2를 입력받아 정수 나눗셈 연산을 수행하고 그 몫을 반환합니다.
# 시간/공간 복잡도 : 시간복잡도 O(1), 공간복잡도 O(1)

def solution(num1, num2):
    answer = num1 // num2
    return answer