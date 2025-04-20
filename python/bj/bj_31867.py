# 문제 링크 : https://www.acmicpc.net/problem/31867
# 간단한 문제 설명 : 주어진 정수 K의 각 자릿수가 짝수인지 홀수인지 판별하여, 짝수의 개수와 홀수의 개수를 비교하고, 그 결과에 따라 0, 1, 또는 -1을 출력
# 해결 방법 설명 : K의 각 자릿수를 순회하며 짝수와 홀수의 개수를 세어봅니다.
# 시간/공간 복잡도 : O(N)

# 입력 처리
N = int(input())
K = input()

# 짝수와 홀수 개수 계산
even_count = 0
odd_count = 0
for digit in K:
    if int(digit) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# 결과 출력
if even_count > odd_count:
    print(0)
elif odd_count > even_count:
    print(1)
else:
    print(-1)