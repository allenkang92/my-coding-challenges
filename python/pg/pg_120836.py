# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 간단한 문제 설명 : 
#   자연수 n이 주어질 때, 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 반환합니다.
#
# 해결 방법 설명 :
#   - 1부터 n까지 반복하며, n이 해당 수로 나누어 떨어지면 (i, n//i)를 순서쌍으로 간주합니다.
#   - 모든 순서쌍의 개수를 계산하여 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n)
#   - 공간 복잡도: O(n) (순서쌍을 저장할 리스트 사용)

def solution(n):
    answer = []
    for i in range(1, n + 1):
        # n이 i로 나누어 떨어지는지 확인 (나머지가 없는 경우)
        if n % i == 0:
            answer.append((i, n // i))
    return len(answer)