# 문제 링크 : https://www.acmicpc.net/problem/17356
# 간단한 문제 설명 : 욱의 욱제력 A와 제의 욱제력 B가 주어질 때, 욱이 제를 이길 확률을 계산하는 문제입니다.
#
# 해결 방법 설명 :            
#   M = (B - A) / 400 으로 정의하고, 확률은 1 / (1 + 10**M) 으로 계산합니다.
#
# 시간/공간 복잡도 : O(1)

A, B = map(int, input().split())

M = (B - A) / 400
Win_pro_A = 1 / (1 + (10 ** M))

print(Win_pro_A)