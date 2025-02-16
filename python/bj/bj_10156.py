# 문제 링크 (주석) : https://www.acmicpc.net/problem/10156
# 문제 설명:
#   과자 한 개의 가격 K, 사려고 하는 과자의 개수 N, 현재 동수가 가진 돈 M이 주어질 때,
#   동수가 부모님께 받아야 하는 모자란 돈을 계산하는 문제입니다.
#
# 해결 방법 설명:
#   과자의 총 가격은 K * N 입니다.
#   만약 현재 가진 돈 M이 총 가격보다 적으면, 그 차액(total_cost - M)을 출력하고,
#   그렇지 않으면 0을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

K, N, M = map(int, input().split())
total_cost = K * N

if M >= total_cost:
    print(0)
else:
    print(total_cost - M)