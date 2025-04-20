# 문제 링크 : https://www.acmicpc.net/problem/13136
# 간단한 문제 설명 : R×C 크기의 좌석을 N×N 크기의 CCTV로 모두 촬영하려고 합니다. 필요한 최소 CCTV 개수를 구하세요.
# 해결 방법 설명 : 각 차원(가로, 세로)을 N으로 나누고, 올림하여 필요한 CCTV 개수를 계산합니다.
# 시간/공간 복잡도 : O(1)

# R, C, N 입력
R, C, N = map(int, input().split())

# 필요한 CCTV 개수 계산 (올림 연산 없이 구현)
cctv_rows = (R + N - 1) // N
cctv_cols = (C + N - 1) // N
total_cctv = cctv_rows * cctv_cols

# 결과 출력
print(total_cctv)