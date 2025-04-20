# 문제 링크 : https://www.acmicpc.net/problem/10872
# 간단한 문제 설명 : 0보다 크거나 같은 정수 N이 주어질 때, N!을 출력
# 해결 방법 설명 : 반복문을 통해 1부터 N까지 차례로 곱셈하여 팩토리얼 계산
# 시간/공간 복잡도 : O(N) / O(1)

N = int(input())

fac = 1

for i in range(1, N + 1):
    if N == 0:
        print(1)
        break
    else:
        fac *= i

print(fac)