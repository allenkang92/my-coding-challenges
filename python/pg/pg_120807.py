# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120807
# 간단한 문제 설명 : 정수 num1과 num2가 주어질 때, 두 수가 같으면 1, 다르면 -1을 반환하는 함수를 작성하세요.
# 해결 방법 설명 : num1과 num2를 비교하여 같으면 1을, 다르면 -1을 반환합니다.
# 시간/공간 복잡도 : 시간복잡도 O(1), 공간복잡도 O(1)

def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1