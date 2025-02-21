# 문제 링크 (주석) : https://www.acmicpc.net/problem/26592
# 문제 설명:
#   수학 선생님께서 삼각형의 넓이와 밑변의 길이가 주어졌을 때 삼각형의 높이를 구하는 프로그램을 요청하셨습니다.
#   삼각형의 넓이 공식: area = (height * base) / 2
#   따라서, height = (2 * area) / base 입니다.
#
# 입력:
#   첫 번째 줄에 데이터 세트의 수 n이 주어집니다.
#   이후 n개의 줄에 걸쳐, 삼각형의 넓이와 밑변 길이가 공백으로 구분되어 주어집니다.
#
# 출력:
#   각 데이터 세트에 대해 삼각형의 높이를 소수점 둘째 자리까지 반올림하여,
#   "The height of the triangle is #.## units" 형식으로 출력합니다.
#
# 시간/공간 복잡도 : O(n)

n = int(input())
for _ in range(n):
    area, base = map(float, input().split())
    height = (2 * area) / base
    print(f"The height of the triangle is {height:.2f} units")