# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181831
# 간단한 문제 설명 : n x n 크기의 이차원 배열에서 arr[i][j] = arr[j][i]가 모든 i,j에 
#                  대해 성립하는지 확인합니다.
# 해결 방법 설명 : 모든 원소에 대해 대칭되는 위치의 값이 같은지 확인하고,
#                하나라도 다르면 0을 반환합니다.
# 시간/공간 복잡도 : O(n²) (n x n 배열의 모든 원소 확인)

def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:  # 대칭 위치의 값이 다르면
                return 0                 # 0 반환
    return 1                            # 모든 위치가 같으면 1 반환