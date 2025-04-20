# 문제 링크 : https://www.acmicpc.net/problem/21665
# 간단한 문제 설명 : 원본 이미지와 네거티브 이미지를 비교하여 잘못된 픽셀의 개수를 찾는 문제
# 해결 방법 설명 : 원본 이미지와 네거티브 이미지를 픽셀 단위로 비교하여 잘못된 픽셀의 개수를 계산
# 시간/공간 복잡도 : O(n * m) (이미지의 크기에 비례하는 시간과 공간이 소요됨)

# 입력 받기
n, m = map(int, input().split())  # 이미지의 높이와 너비

# 원본 이미지 입력
original = [input().strip() for _ in range(n)]

# 빈 줄 건너뛰기
input()

# 네거티브 이미지 입력
negative = [input().strip() for _ in range(n)]

# 잘못된 픽셀 개수 계산
error_count = 0
for i in range(n):
    for j in range(m):
        # 원본 픽셀과 네거티브 픽셀 비교
        if original[i][j] == negative[i][j]:
            error_count += 1

# 결과 출력
print(error_count)