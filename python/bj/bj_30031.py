# 문제 링크 : https://www.acmicpc.net/problem/30031
# 문제 설명:
#   대한민국 지폐는 천 원권, 오천 원권, 만 원권, 오만 원권으로 총 네 종류가 있다.
#   각 지폐의 세로 길이는 68mm로 모두 같지만, 가로 길이는 모두 다르다.
#   천 원권: 136mm, 오천 원권: 142mm, 만 원권: 148mm, 오만 원권: 154mm
#   주어진 지폐의 가로, 세로 길이를 통해 지폐의 종류를 구별하고 총액을 계산하는 문제이다.
#
# 입력:
#   첫 번째 줄에 지폐의 개수 N (1 ≤ N ≤ 100)이 주어진다.
#   이후 N개의 줄에 걸쳐 각 지폐의 가로, 세로 길이가 정수로 주어진다.
#   (길이는 천 원권, 오천 원권, 만 원권, 오만 원권의 길이 중 하나이다.)
#
# 출력:
#   수민이가 가진 지폐의 총액을 출력한다.
#
# 해결 방법:
#   각 지폐의 가로 길이를 확인하여 해당 지폐의 금액을 더해준다.
#
# 시간/공간 복잡도: O(N)

N = int(input())
count = 0

for _ in range(N):
    dimensions = list(map(int, input().split()))
    # dimensions[0] : 가로 길이, dimensions[1] : 세로 길이 (여기서는 세로 길이는 항상 68)
    if dimensions[0] == 136:
        count += 1000
    elif dimensions[0] == 142:
        count += 5000
    elif dimensions[0] == 148:
        count += 10000
    elif dimensions[0] == 154:
        count += 50000

print(count)