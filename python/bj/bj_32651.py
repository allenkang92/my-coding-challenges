# 문제 링크 : https://www.acmicpc.net/problem/32651
# 간단한 문제 설명:
#   형진이는 2024년을 기념하며 100,000 이하인 2024의 배수를 기억해 두었다.
#   양의 정수 N이 입력으로 주어졌을 때, N이 2024의 배수면서 100,000 이하이면 "Yes"를,
#   그렇지 않으면 "No"를 출력하는 문제입니다.
#
# 해결 방법 설명:
#   if 조건문을 사용하여 N이 2024로 나누어 떨어지면서 N이 100,000 이하인지 확인합니다.
#
# 시간/공간 복잡도 : O(1)

N = int(input())

if N % 2024 == 0 and N <= 100000:
    print("Yes")
else:
    print("No")