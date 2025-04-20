# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120897
# 간단한 문제 설명:
#   정수 n의 약수를 오름차순으로 담은 배열을 반환합니다.
#
# 해결 방법 설명:
#   - 1부터 n까지 반복하면서, 각 숫자가 n의 약수인지 확인합니다.
#     (즉, n을 해당 숫자로 나눈 나머지가 0이면 약수입니다.)
#   - 약수인 경우 결과 리스트(answer)에 추가합니다.
#   - 최종적으로 answer에 담긴 약수들을 오름차순으로 반환합니다.
#
# 시간/공간 복잡도:
#   - 시간 복잡도: O(n)
#   - 공간 복잡도: O(n)

def solution(n):
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:  # n이 i로 나누어 떨어지면 i는 n의 약수입니다.
            answer.append(i)
    return answer