# 문제 링크 : https://www.acmicpc.net/problem/25377
# 간단한 문제 설명 : 여러 가게 중에서 KOI 빵을 구매할 수 있는 가장 빠른 시간을 찾는 문제
# 해결 방법 설명 : 각 가게에 대해 A <= B인 경우 중 가장 작은 B 값을 찾음
# 시간/공간 복잡도 : O(N) (가게의 수에 비례하여 시간과 공간이 소요됨)

# 입력 받기
N = int(input())  # 가게의 수
stores = [tuple(map(int, input().split())) for _ in range(N)]  # 각 가게의 A, B 값

# 가능한 가게 중 가장 작은 B 값 찾기
min_time = float('inf')
for A, B in stores:
    if A <= B:
        if B < min_time:
            min_time = B

# 결과 출력
if min_time != float('inf'):
    print(min_time)
else:
    print(-1)