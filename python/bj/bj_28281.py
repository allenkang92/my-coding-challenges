# 문제 링크 : https://www.acmicpc.net/problem/28281
# 간단한 문제 설명 : 연속된 이틀 동안 매일 X개의 양말을 사는 데 드는 최소 비용을 계산
# 해결 방법 설명 : 연속된 이틀 동안의 양말 구매 비용을 계산하고, 그 중 최소 비용을 찾음
# 시간/공간 복잡도 : O(N) (N일에 비례하여 시간과 공간이 소요됨)

# 입력 받기
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 최소 비용 초기화
min_cost = float('inf')

# 연속된 이틀 동안의 비용 계산
for i in range(N - 1):
    cost = (A[i] + A[i + 1]) * X
    if cost < min_cost:
        min_cost = cost

# 결과 출력
print(min_cost)