# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181901
# 간단한 문제 설명 : 정수 n과 k가 주어졌을 때, 1 이상 n 이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 반환합니다.
# 해결 방법 설명 : k부터 n까지 k 간격으로 반복하면서 해당 값을 배열에 추가합니다.
# 시간/공간 복잡도 : O(n/k)

def solution(n, k):
    answer = []
    # k부터 n까지 k 간격으로 값들을 추가
    for i in range(k, n+1, k):
        answer.append(i)
    return answer