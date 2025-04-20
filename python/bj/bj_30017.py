# 문제 링크 : https://www.acmicpc.net/problem/30017
# 간단한 문제 설명 : 주어진 패티와 치즈의 개수를 바탕으로, 최대 크기의 치즈버거를 만듦
# 해결 방법 설명 : 패티와 치즈의 개수를 고려하여 가능한 최대 크기를 계산
# 시간/공간 복잡도 : O(1) (상수 시간과 공간이 소요됨)

# 입력 처리
A, B = map(int, input().split())

# 최대 치즈버거 크기 계산
max_patties = min(A, B + 1)
max_cheese = min(A - 1, B)
max_size = max_patties + max_cheese

# 결과 출력
print(max_size)