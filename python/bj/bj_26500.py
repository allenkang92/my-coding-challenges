# 문제 링크 (주석) : https://www.acmicpc.net/problem/26500
# 문제 설명:
#   두 실수 값이 주어졌을 때, 두 값 사이의 절대 선 거리(absolute line distance)를 구하여,
#   소수점 첫째 자리까지 반올림한 후, 정확히 한 자리의 소수점 값을 출력하는 문제입니다.
#
# 해결 방법:
#   각 데이터 세트마다 두 값을 입력받아, 두 값의 차이의 절대값을 구한 후,
#   round() 함수와 형식 지정을 이용해 소수점 첫째 자리까지 출력합니다.
#
# 시간/공간 복잡도 : O(n)

n = int(input())
for _ in range(n):
    a, b = map(float, input().split())
    print(f"{abs(b - a):.1f}")