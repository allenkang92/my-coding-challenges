# 문제 링크 : https://www.acmicpc.net/problem/31962
# 간단한 문제 설명 : 정올이가 학교에 지각하지 않기 위해 X분 이내로 도착할 수 있는 버스 중에서, 가장 늦게 출발하는 버스가 출발할 때까지 걸리는 시간을 찾는 문제
# 해결 방법 설명 : 각 버스에 대해 S + T <= X인지 확인하고, 가능한 버스 중 가장 늦게 출발하는 버스의 S를 찾음
# 시간/공간 복잡도 : O(N)

# 입력 처리
N, X = map(int, input().split())
buses = []
for _ in range(N):
    S, T = map(int, input().split())
    buses.append((S, T))

# 가능한 버스 중 가장 늦게 출발하는 버스 찾기
max_S = -1
for S, T in buses:
    if S + T <= X and S > max_S:
        max_S = S

# 결과 출력
print(max_S)