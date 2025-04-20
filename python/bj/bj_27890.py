# 문제 링크 : https://www.acmicpc.net/problem/27890
# 간단한 문제 설명 : 분수의 높이가 특정 규칙에 따라 변화할 때, 주어진 시간 N에서의 분수 높이를 계산
# 해결 방법 설명 : 주어진 규칙에 따라 N초까지 분수의 높이를 계산
# 시간/공간 복잡도 : O(N) (N초에 비례하여 시간과 공간이 소요됨)

# 입력 받기
x0, N = map(int, input().split())

# 높이 계산
x = x0
for _ in range(N):
    if x % 2 == 0:
        x = (x // 2) ^ 6
    else:
        x = (2 * x) ^ 6

# 결과 출력
print(x)