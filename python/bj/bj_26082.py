# 문제 링크 : https://www.acmicpc.net/problem/26082
# 간단한 문제 설명 :
#   경쟁사 제품의 가격 A, 경쟁사 제품의 성능 B, WARBOY의 가격 C가 주어질 때,
#   경쟁사 제품의 가격 대비 성능은 B / A 이며, WARBOY는 가격 대비 성능이 경쟁사 제품의 3배입니다.
#   따라서 WARBOY의 성능은 WARBOY의 가격 C와 경쟁사 대비 3배의 가격 대비 성능을 곱한 값입니다.
#
# 해결 방법 설명 :
#   1) 경쟁사 제품의 가격 대비 성능을 계산합니다: R_price_perfomance = B / A
#   2) WARBOY의 가격 대비 성능은 3배이므로, W_price_perfomance = 3 * R_price_perfomance
#   3) WARBOY의 성능은 WARBOY의 가격 C와 W_price_perfomance의 곱으로 계산됩니다.
#
# 시간/공간 복잡도 : O(1)

A, B, C = map(int, input().split(" "))

R_price_perfomance = B / A       # 경쟁사 제품의 가격 대비 성능
W_price_perfomance = 3 * R_price_perfomance  # WARBOY의 가격 대비 성능 (경쟁사 제품의 3배)
W_perfomance = W_price_perfomance * C        # WARBOY의 성능 = WARBOY의 가격 * WARBOY의 가격 대비 성능

print(int(W_perfomance))