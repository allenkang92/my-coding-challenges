# 문제 링크 : https://www.acmicpc.net/problem/20833
# 문제 설명:
#   Nadja는 한 변의 길이가 1인 작은 큐브들을 이어 붙여서 한 변의 길이가 1부터 N까지인
#   각각의 큰 큐브를 만들고자 합니다.
#   각 큐브를 만드는데 필요한 작은 큐브의 개수는 부피와 같으므로, 1^3, 2^3, ..., N^3 의 합을 구하면 됩니다.
#
# 해결 방법 설명:
#   1부터 N까지의 정수 i에 대해 i^3의 합을 계산한 후 출력합니다.
#
# 시간/공간 복잡도 : O(N)

N = int(input())

total_cube = 0
for i in range(1, N+1):
    total_cube += i ** 3

print(total_cube)