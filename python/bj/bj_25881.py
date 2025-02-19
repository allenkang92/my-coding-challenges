# 문제 링크 (주석) : https://www.acmicpc.net/problem/25881
# 문제 설명:
#   고객들이 사용한 전기 사용량에 따라 전기요금을 계산하는 문제입니다.
#   전기 회사는 에너지 절약을 위해 처음 1000 KWH까지는 낮은 요율,
#   그 이후는 높은 요율을 적용합니다.
#
#   첫 번째 입력 줄에는 처음 1000 KWH 사용에 대한 요율와 추가 사용 요율이 주어집니다.
#   그 다음 줄에는 고객의 수가 주어지고, 이후 각 줄마다 고객의 전기 사용량(1 ~ 50000)이 주어집니다.
#
#   각 고객에 대해 사용량과 전기요금을 공백으로 구분하여 출력합니다.
#
# 해결 방법:
#   - 만약 고객의 사용량이 1000 KWH 이하이면, 요금 = 사용량 × 첫 번째 요율
#   - 만약 고객의 사용량이 1000 KWH를 초과하면,
#       요금 = (1000 × 첫 번째 요율) + ((사용량 - 1000) × 두 번째 요율)
#
# 시간/공간 복잡도 : O(n)

d, extra_rate = map(int, input().split(" "))
customer_count = int(input())

for _ in range(customer_count):
    usage = int(input())
    if usage <= 1000:
        bill = usage * d
    else:
        bill = (1000 * d) + ((usage - 1000) * extra_rate)
    print(usage, bill)