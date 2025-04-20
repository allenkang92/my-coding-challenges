# 문제 링크 : https://codeup.kr/problem.php?id=6044
# 간단한 문제 설명 : 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산하여 출력합니다.
# 해결 방법 설명 : 1. input().split()으로 두 수를 분리합니다.
#                2. map(int, ...)를 사용하여 각 수를 정수로 변환합니다.
#                3. 각 연산 결과를 출력합니다.
# 시간/공간 복잡도 : O(1) (단순 입출력 및 산술 연산)

i1, i2 = map(int, input().split())

print(i1 + i2)
print(i1 - i2)
print(i1 * i2)
print(i1 // i2)
print(i1 % i2)
print(format(i1 / i2, ".2f"))