# 문제 링크 : https://www.acmicpc.net/problem/28701
# 간단한 문제 설명 :
#   1부터 N까지의 정수에 대해 다음 세 가지 값을 차례대로 출력하는 문제입니다.
#     1) 1부터 N까지 정수의 합, 즉 sum = 1+2+...+N
#     2) 1부터 N까지 정수의 합을 제곱한 값, 즉 sum^2
#     3) 1부터 N까지 정수의 세제곱의 합, 즉 1^3+2^3+...+N^3
#
# 해결 방법 설명 :
#   먼저 for문을 사용하여 1부터 N까지의 합을 구하고, 이를 제곱하여 두 번째 값을 계산합니다.
#   이어서 또 다른 for문을 사용하여 1부터 N까지 각 정수의 세제곱을 누적하여 합산합니다.
#
# 시간/공간 복잡도 : O(N)

N = int(input())  # 정수 N 입력 (5 ≤ N ≤ 100)

sum_result = 0           # 1부터 N까지 정수의 합을 저장할 변수
sum_square_result = 0    # sum_result의 제곱값을 저장할 변수 (1부터 N까지 정수의 합의 제곱)
sum_3square_result = 0   # 1부터 N까지 각 정수의 세제곱의 합을 저장할 변수

# 1부터 N까지 정수의 합을 구함
for i in range(1, N+1):
    sum_result += i

# 정수의 합을 제곱하여 저장
sum_square_result = (sum_result ** 2)

# 1부터 N까지 각 정수의 세제곱의 합을 구함
for i in range(1, N+1):
    sum_3square_result += i ** 3

# 결과 출력:
# 첫 줄에 1부터 N까지의 합, 둘째 줄에 그 합의 제곱, 셋째 줄에 1부터 N까지의 세제곱의 합을 순서대로 출력합니다.
print(sum_result)
print(sum_square_result)
print(sum_3square_result)