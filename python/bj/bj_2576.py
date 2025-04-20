# 문제 링크 : https://www.acmicpc.net/problem/2576
# 문제 설명:
#   7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고,
#   고른 홀수들 중 최솟값을 찾는 프로그램을 작성한다.
#   만약 홀수가 하나도 없으면 -1을 출력한다.
#
# 입력:
#   7개의 자연수가 한 줄에 하나씩 주어진다. (자연수는 100보다 작다)
#
# 출력:
#   홀수가 존재하면 첫째 줄에 홀수들의 합을, 둘째 줄에 홀수들 중 최솟값을 출력한다.
#   홀수가 없으면 첫째 줄에 -1을 출력한다.
#
# 해결 방법:
#   입력받은 7개의 수 중 홀수만을 골라 리스트에 저장한 후, 리스트의 합과 최솟값을 구한다.
#
# 시간/공간 복잡도: O(7) → O(1)

n_list = []
for _ in range(7):
    n_list.append(int(input()))

odd_list = []
for n in n_list:
    if n % 2 != 0:
        odd_list.append(n)

if len(odd_list) == 0:
    print(-1)
else:
    print(sum(odd_list))
    print(min(odd_list))