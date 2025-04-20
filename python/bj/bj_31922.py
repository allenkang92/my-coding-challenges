# 문제 링크 : https://www.acmicpc.net/problem/31922
# 간단한 문제 설명 : Division 1, Division 2, shake! 대회의 우승 상금이 주어졌을 때, 최대 상금을 계산
# 해결 방법 설명 : Division 1과 shake! 대회의 상금을 합치거나, Division 2의 상금만 고려하여 최대값을 선택
# 시간/공간 복잡도 : O(1)

# 입력 처리
A, P, C = map(int, input().split())

# 최대 상금 계산
max_prize = max(A + C, P)

# 결과 출력
print(max_prize)