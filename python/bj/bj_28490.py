# 문제 링크 : https://www.acmicpc.net/problem/28490
# 문제 설명:
#   Stuart는 n개의 직사각형 액자(frame)를 가지고 있습니다.
#   각 액자 i는 높이 h[i]와 너비 w[i]를 가지고 있으며,
#   액자의 크기는 그 액자가 차지하는 면적(h[i] * w[i])입니다.
#   n개의 액자 중에서 가장 큰 면적을 출력하는 프로그램을 작성하세요.
#
# 입력:
#   첫 번째 줄에 액자의 개수 n이 주어집니다.
#   이후 n개의 각 줄에 두 정수 h[i]와 w[i]가 공백으로 구분되어 주어집니다.
#
# 출력:
#   가장 큰 액자의 면적을 나타내는 정수를 출력합니다.
#
# 시간/공간 복잡도 : O(n)

n = int(input())
max_area = 0
for _ in range(n):
    h, w = map(int, input().split())
    area = h * w
    if area > max_area:
        max_area = area

print(max_area)