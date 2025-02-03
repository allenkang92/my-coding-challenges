# 문제 링크 (주석) : https://www.acmicpc.net/problem/10810
# 간단한 문제 설명 : 
#   N개의 바구니와 M번의 공 넣기 시도
#   각 시도마다 i부터 j까지의 바구니에 k번 공을 넣음
#
# 해결 방법 설명 : 
#   - N개의 바구니를 0으로 초기화
#   - M번 반복하면서:
#     - i, j, k를 입력받음
#     - i부터 j까지의 바구니에 k를 넣음
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N*M) - M번의 시도에서 최대 N개의 바구니 수정
#   - 공간 복잡도: O(N) - N개의 바구니 저장

N, M = map(int, input().split())
basket = [0] * N  # N개의 바구니를 0으로 초기화

for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):  # i-1부터 j-1까지 (인덱스는 0부터 시작)
        basket[idx] = k

print(*basket)  # 리스트를 공백으로 구분하여 출력