# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 간단한 문제 설명 : 
#   정수 n이 주어질 때, n 이하의 모든 짝수를 더한 값을 반환하는 문제입니다.
#
# 해결 방법 설명 :
#   - 0부터 n까지 반복하면서 짝수(2로 나눈 나머지가 0인 수)를 찾아 리스트에 저장합니다.
#   - 저장된 짝수들의 합을 계산하여 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n) - n까지 반복
#   - 공간 복잡도: O(n) - 짝수를 저장할 리스트 사용 (최악의 경우 n/2개 원소)

def solution(n):
    answer = []
    for e in range(n + 1):
        if e % 2 == 0:
            answer.append(e)
    return sum(answer)