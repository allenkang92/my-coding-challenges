# 문제 링크 : https://www.acmicpc.net/problem/29683
# 간단한 문제 설명 : 각 고객의 구매 금액에 따라 로또 티켓을 몇 장 발급해야 하는지 계산
# 해결 방법 설명 : 각 체크의 구매 금액을 A로 나눈 몫을 계산하여 총 티켓 수를 구함
# 시간/공간 복잡도 : O(n) (체크 수에 비례하여 시간과 공간이 소요됨)

# 입력 받기
n, A = map(int, input().split())
purchases = list(map(int, input().split()))

# 총 티켓 수 계산
total_tickets = sum(purchase // A for purchase in purchases)

# 결과 출력
print(total_tickets)