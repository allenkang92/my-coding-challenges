# 문제 링크 : https://www.acmicpc.net/problem/14489
# 문제 설명:
#   욱제에게는 두 개의 통장이 있으며, 두 통장의 잔고와 치킨 한 마리의 가격이 주어집니다.
#   만약 두 통장 잔고의 합이 치킨 두 마리의 가격(2 * C) 이상이면,
#   치킨을 구입한 후 남은 잔고의 합을 출력하고, 그렇지 않으면 현재 두 통장의 잔고의 합을 출력합니다.
#
# 해결 방법 설명:
#   두 통장의 잔고의 합을 계산한 후, 치킨 두 마리의 총 비용(2 * C)과 비교합니다.
#   잔고가 충분하면 남은 잔고를, 부족하면 현재 잔고의 합을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

A, B = map(int, input().split())
C = int(input())

total_balance = A + B
total_cost = C * 2

if total_balance >= total_cost:
    print(total_balance - total_cost)
else:
    print(total_balance)