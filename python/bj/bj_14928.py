# 문제 링크 (주석) : https://www.acmicpc.net/problem/14928
# 간단한 문제 설명 : 큰 수를 20000303으로 나눈 나머지를 구하는 프로그램
# 해결 방법 설명 : 문자열로 입력받아 Horner's method를 이용하여 나머지 계산
# 시간/공간 복잡도 : O(N), N은 입력 숫자의 자릿수

N = input()
remainder = 0
for digit in N:
    remainder = (remainder * 10 + int(digit)) % 20000303

print(remainder)