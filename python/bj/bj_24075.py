# 문제 링크 (주석) : https://www.acmicpc.net/problem/24075
# 문제 설명:
#   두 정수 A, B가 주어질 때, A+B와 A-B 중에서 가장 큰 값과 가장 작은 값을
#   순서대로 출력하는 문제입니다.
#
# 해결 방법 설명:
#   A+B와 A-B를 각각 계산한 후, 둘 중 최댓값과 최솟값을 구하여 출력합니다.
#
# 시간/공간 복잡도 : O(1)

A, B = map(int, input().split(" "))

sum_value = A + B
sub_value = A - B

print(max(sum_value, sub_value))
print(min(sum_value, sub_value))