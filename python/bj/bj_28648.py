# 문제 링크 : https://www.acmicpc.net/problem/28648
# 간단한 문제 설명 : 여러 버스 중에서 가장 빨리 도착할 수 있는 시간을 계산
# 해결 방법 설명 : 각 버스의 도착 시간을 계산하고, 가장 작은 값을 찾음
# 시간/공간 복잡도 : O(n) (n은 버스의 수)

# 입력 받기
n = int(input())
buses = [tuple(map(int, input().split())) for _ in range(n)]

# 도착 시간 계산
min_time = min(t + l for t, l in buses)

# 결과 출력
print(min_time)