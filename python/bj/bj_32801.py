# 문제 링크 (주석) : https://www.acmicpc.net/problem/32801
# 간단한 문제 설명 : 일반화된 FizzBuzz 문제에서 "Fizz", "Buzz", "FizzBuzz"가 각각 몇 번 출력되는지 계산
# 해결 방법 설명 : a와 b의 최소공배수를 구하고, 각 조건에 맞는 숫자의 개수를 계산
# 시간/공간 복잡도 : O(1)

import math

# 입력 처리
n, a, b = map(int, input().split())

# 최소공배수(LCM) 계산
lcm = a * b // math.gcd(a, b)

# "FizzBuzz"의 개수 계산
fizzbuzz_count = n // lcm

# "Fizz"의 개수 계산
fizz_count = n // a - fizzbuzz_count

# "Buzz"의 개수 계산
buzz_count = n // b - fizzbuzz_count

# 결과 출력
print(fizz_count, buzz_count, fizzbuzz_count)