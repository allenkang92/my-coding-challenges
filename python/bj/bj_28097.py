# 문제 링크 : https://www.acmicpc.net/problem/28097
# 간단한 문제 설명 : 포닉스가 N개의 공부 계획을 순서대로 실행하고, 각 계획 사이에 8시간의 휴식을 취할 때, 총 소요 시간을 일과 시간 단위로 계산
# 해결 방법 설명 : 모든 공부 시간과 휴식 시간을 합산하고, 일과 시간으로 변환
# 시간/공간 복잡도 : O(N) (N개의 공부 계획에 비례하여 시간과 공간이 소요됨)

# 입력 받기
N = int(input())
T = list(map(int, input().split()))

# 총 시간 계산
total_time = sum(T) + (N - 1) * 8

# 일과 시간으로 변환
days = total_time // 24
hours = total_time % 24

# 결과 출력
print(days, hours)