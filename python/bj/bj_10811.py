# 문제 링크 (주석) : https://www.acmicpc.net/problem/10811
# 간단한 문제 설명 : 
#   N개의 바구니에서 M번 구간을 역순으로 만드는 프로그램
#   각 바구니에는 1부터 N까지 번호가 순서대로 있음
#
# 해결 방법 설명 : 
#   1. N개의 바구니를 1부터 N까지 초기화
#   2. M번 반복하면서:
#      - i, j 구간을 입력받음
#      - i-1부터 j까지의 구간을 슬라이싱하여 역순으로 변경
#   3. 최종 결과 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N*M) - M번의 역순 연산
#   - 공간 복잡도: O(N) - N개의 바구니 저장

N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = reversed(basket[i-1:j])  # i-1부터 j-1까지 역순으로

print(*basket)