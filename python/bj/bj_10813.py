# 문제 링크 : https://www.acmicpc.net/problem/10813
# 간단한 문제 설명 : 
#   N개의 바구니에서 M번 공을 교환하는 프로그램
#   초기에는 i번 바구니에 i번 공이 있음
#   M번의 교환 후 최종 상태 출력
#
# 해결 방법 설명 : 
#   1. N개의 바구니를 초기화 (1부터 N까지의 숫자로)
#   2. M번 반복하면서:
#      - i, j 위치의 공을 교환
#      - basket[i-1], basket[j-1] 사용 (인덱스는 0부터 시작하므로 1 빼기)
#   3. 결과를 공백으로 구분하여 출력 (*basket 사용)
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(M) - M번의 교환 연산
#   - 공간 복잡도: O(N) - N개의 바구니 저장

N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]  # 1부터 N까지 초기화

for _ in range(M):
    i, j = map(int, input().split())
    # 파이썬의 다중 할당으로 두 위치의 값을 교환
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)  # * 연산자로 리스트를 언패킹하여 공백으로 구분된 형태로 출력