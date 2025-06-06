# 문제 링크 : https://www.acmicpc.net/problem/21631
# 간단한 문제 설명 : 흰색과 검은색 조각을 쌓아 탑을 만들 때, 검은색 줄무늬의 최대 개수를 구하는 문제
# 해결 방법 설명 : 검은색 줄무늬의 개수는 검은색 조각의 개수와 흰색 조각의 개수 + 1 중 작은 값
# 시간/공간 복잡도 : O(1) (입력 크기에 관계없이 일정한 시간과 공간이 소요됨)

# 입력 받기
a, b = map(int, input().split())

# 최대 검은색 줄무늬 개수 계산
max_stripes = min(b, a + 1)

# 결과 출력
print(max_stripes)