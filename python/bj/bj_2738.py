# 문제 링크 (주석) : https://www.acmicpc.net/problem/2738
# 간단한 문제 설명 : N*M 크기의 두 행렬을 입력받아 더하는 문제
# 해결 방법 설명 : 두 행렬을 2차원 리스트로 저장하고 각 위치의 원소를 더함
# 시간/공간 복잡도 : O(N*M) - 모든 행렬 원소를 한 번씩 처리

N, M = map(int, input().split())

# 첫 번째 행렬 A 입력 받기
A = []
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 두 번째 행렬 B 입력 받기
B = []
for i in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 두 행렬의 합 계산
result = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    result.append(row)

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))