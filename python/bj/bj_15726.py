# 문제 링크 (주석) : https://www.acmicpc.net/problem/15726
# 문제 설명:
#   세 수 A, B, C가 주어질 때, 한 번의 곱셈 기호와 한 번의 나눗셈 기호를 이용하여 
#   "A ☐ B ☐ C" 형태의 식을 만들었을 때 가능한 가장 큰 값을 구하는 문제입니다.
#   두 가지 경우는 다음과 같습니다.
#       1) (A * B) / C
#       2) (A / B) * C
#   소수점 이하의 숫자는 버립니다.
#
# 시간/공간 복잡도 : O(1)

A, B, C = map(int, input().split())

case1 = A * B / C
case2 = A / B * C

print(int(max(case1, case2)))