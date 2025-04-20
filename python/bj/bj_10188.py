# 문제 링크 : https://www.acmicpc.net/problem/10188
# 문제 설명:
#   주어진 데이터 셋마다, 두 개의 정수(길이와 너비)가 주어진다.
#   이때, 대문자 X를 이용하여 해당 크기의 사각형(4면의 도형)을 출력하는 문제입니다.
#   모든 사각형은 빈 줄로 구분되어 출력되어야 합니다.
#
# 해결 방법 설명:
#   각 데이터 셋에 대해, 너비(세로 길이)만큼 반복하며 한 줄에 X를 길이(가로 길이)만큼 출력합니다.
#   각 사각형 사이에는 빈 줄을 추가합니다.
#
# 시간/공간 복잡도 : O(n) per 데이터 셋

T = int(input())

for i in range(T):
    length, width = map(int, input().split())
    for _ in range(width):
        print("X" * length)
    if i < T - 1:
        print()