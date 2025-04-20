# 문제 링크 : https://www.acmicpc.net/problem/17874
# 간단한 문제 설명 : 정사각형 케이크를 수평과 수직으로 한 번씩 자른 후, 가장 큰 조각의 부피를 계산하는 문제
# 해결 방법 설명 : 절단 위치에 따라 네 조각의 가로와 세로 길이를 계산하고, 가장 큰 면적을 가진 조각의 부피를 계산
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
n, h, v = map(int, input().split())  # 케이크의 한 변의 길이, 수평 절단 위치, 수직 절단 위치

# 네 조각의 가로와 세로 길이 계산
piece1_width = v
piece1_height = h

piece2_width = n - v
piece2_height = h

piece3_width = v
piece3_height = n - h

piece4_width = n - v
piece4_height = n - h

# 가장 큰 면적 계산
max_area = max(
    piece1_width * piece1_height,
    piece2_width * piece2_height,
    piece3_width * piece3_height,
    piece4_width * piece4_height
)

# 가장 큰 조각의 부피 계산 (면적 × 두께 4cm)
max_volume = max_area * 4

# 결과 출력
print(max_volume)