# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 간단한 문제 설명 : 정수 n이 주어질 때, n 이하의 홀수를 오름차순으로 담은 배열을 반환하는 함수를 작성하세요.
# 해결 방법 설명 : 
#   1. 1부터 n까지의 범위에서 2씩 증가하며 홀수를 순회합니다.
#   2. 각 홀수를 리스트에 추가합니다.
#   3. 완성된 리스트를 반환합니다.
# 시간/공간 복잡도 : 
#   - 시간복잡도 : O(n) - n의 크기에 비례하여 반복이 수행됩니다.
#   - 공간복잡도 : O(n) - 결과 리스트에 최대 n/2개의 홀수가 저장됩니다.

def solution(n):
    answer = []
    for num in range(1, n+1, 2):
        answer.append(num)
    return answer