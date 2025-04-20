# 문제 링크 : https://www.acmicpc.net/problem/2530
# 문제 설명:
#   현재 시각과 요리하는 데 필요한 시간(초 단위)이 주어졌을 때,
#   요리(오븐구이)가 끝나는 시각을 24시간 시계 형식(시 0~23, 분 0~59, 초 0~59)으로 계산하는 문제이다.
#
# 입력:
#   첫 번째 줄에 현재 시각이 시 A (0 ≤ A ≤ 23), 분 B (0 ≤ B ≤ 59), 초 C (0 ≤ C ≤ 59) 순서대로 주어진다.
#   두 번째 줄에 요리하는 데 필요한 시간 D (0 ≤ D ≤ 500,000)가 초 단위로 주어진다.
#
# 출력:
#   오븐구이가 끝나는 시각의 시, 분, 초를 공백으로 구분하여 출력한다.
#
# 해결 방법:
#   1. 현재 시각을 전체 초로 변경한다: total_seconds = A*3600 + B*60 + C.
#   2. 요리에 걸리는 초 D를 더한다.
#   3. 새로운 시간을 하루의 초(24*3600)로 나눈 나머지를 구한다.
#   4. 그것을 다시 시, 분, 초로 변환한다.
#
# 시간/공간 복잡도: O(1)

A, B, C = map(int, input().split())
D = int(input())

# 현재 시각을 초로 환산
total_seconds = A * 3600 + B * 60 + C

# D초 후의 시각 계산 (하루 = 86400초)
total_seconds = (total_seconds + D) % 86400

# 시, 분, 초로 변환
result_hour = total_seconds // 3600
total_seconds %= 3600
result_minute = total_seconds // 60
result_second = total_seconds % 60

print(result_hour, result_minute, result_second)