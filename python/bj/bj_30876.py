# 문제 링크 (주석) : https://www.acmicpc.net/problem/30876
# 문제 설명:
#   Southern Fuegian Railway는 N개의 역과 N-1개의 철로로 구성되어 있다.
#   각 역 i는 (x_i, y_i)에 위치하며, j번째 철로는 역 j와 역 j+1을 잇는다.
#   철로는 직선 구간이므로, 철로 위의 모든 점은 두 역의 좌표를 선형 보간한 값이다.
#
#   철로 위에서 "가장 남쪽에 있는 점"은 y좌표가 가장 작은 점을 의미하며,
#   직선 구간에서는 그 최소값은 항상 끝점(역) 중 하나의 y좌표와 같다.
#   따라서, N개의 역 중 y좌표가 최소인 역이 Southern Fuegian Railway가 지나가는
#   가장 남쪽 점이 된다.
#
# 입력:
#   첫 번째 줄에 역의 개수 N (1 ≤ N ≤ 1000)이 주어진다.
#   다음 N개의 줄에 걸쳐 각 역의 좌표를 나타내는 두 정수 x_i, y_i가 공백으로 구분되어 주어진다. 
#   (|x_i|, |y_i| ≤ 1000)
#
# 출력:
#   Southern Fuegian Railway가 지나는 가장 남쪽에 있는 점의 x좌표와 y좌표를 공백으로 구분하여 출력한다.
#   이 점은 유일함이 보장된다.
#
# 해결 방법:
#   모든 역의 좌표 중에서 y좌표가 최솟값인 좌표를 찾는다.
#
# 시간/공간 복잡도: O(N)

N = int(input())
position_list = []

for _ in range(N):
    x, y = map(int, input().split())
    position_list.append((x, y))

# y좌표를 기준으로 최소인 점을 찾는다.
min_point = min(position_list, key=lambda point: point[1])
print(min_point[0], min_point[1])