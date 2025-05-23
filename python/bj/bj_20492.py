# 문제 링크 : https://www.acmicpc.net/problem/20492
# 간단한 문제 설명 :
#   대회 상금에 대해 두 가지 경우의 실제 수령액을 계산하는 문제
#   1) 전체 상금의 22%를 제세공과금으로 납부하는 경우
#   2) 상금의 80%를 필요 경비로 인정받고, 나머지 20% 중 22%만 제세공과금으로 납부하는 경우
# 해결 방법 설명 :
#   - 1번 경우: N - (22% of N) = N - (22 * N // 100)
#   - 2번 경우: N - (22% of (20% of N)) = N - ((20 * N // 100) * 22 // 100)
# 시간/공간 복잡도 : O(1)

N = int(input())

case1 = N - (22 * N // 100)
case2 = N - ((20 * N // 100) * 22 // 100)

print(case1, case2)