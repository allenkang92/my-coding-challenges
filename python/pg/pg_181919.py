# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181919
# 간단한 문제 설명 : 임의의 1,000 이하의 양의 정수 n이 주어질 때, 초기값이 n인 콜라츠 수열을 return 합니다.
# 해결 방법 설명 : n이 1이 될 때까지 다음 연산을 반복합니다.
#                  - n이 짝수이면 n을 2로 나눕니다.
#                  - n이 홀수이면 n에 3을 곱하고 1을 더합니다.
#                  수열의 모든 원소를 기록하여 반환합니다.
# 시간/공간 복잡도 : O(n) (콜라츠 수열의 길이에 비례)

def solution(n):
    answer = []
    # n이 1이 될 때까지 반복하면서 수열의 각 원소를 answer에 추가합니다.
    while True:
        answer.append(n)
        if n == 1:
            break
        if n % 2 == 0:  # n이 짝수인 경우
            n = n // 2
        else:           # n이 홀수인 경우
            n = (3 * n) + 1
    return answer