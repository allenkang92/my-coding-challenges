# 문제 링크 : https://www.acmicpc.net/problem/29163
# 간단한 문제 설명 : 주어진 숫자들 중에서 짝수의 개수가 홀수의 개수보다 많으면 "Happy", 그렇지 않으면 "Sad"를 출력
# 시간/공간 복잡도 : O(n)

N = int(input())
numbers = list(map(int, input().split(" ")))

even = 0
odd = 0
for x in numbers:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    print("Happy")
else:
    print("Sad")