# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181829
# 간단한 문제 설명 : 2차원 배열에서 i + j <= k를 만족하는 모든 원소의 합을 구합니다.
# 해결 방법 설명 : 이중 반복문으로 배열을 순회하며 i + j <= k 조건을 확인합니다.
# 시간/공간 복잡도 : O(n*m) (n은 행의 수, m은 열의 수)

def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):  # board[0]의 길이로 수정
            if i + j <= k:
                answer += board[i][j]
    return answer