# 문제 링크 (주석) : https://www.acmicpc.net/problem/30979
# 문제 설명:
#   파댕이는 사탕을 먹으면 일정 시간 동안 울지 않는다.
#   여러분은 파댕이를 T분 동안 돌봐야 하며, N개의 사탕을 가지고 있다.
#   각 사탕은 맛의 값 F에 따라 F분 동안 파댕이가 울지 않게 만든다.
#   파댕이가 T분 동안 울지 않도록 할 수 있는지 판단하여,
#   가능하면 "Padaeng_i Happy", 불가능하면 "Padaeng_i Cry"를 출력하는 프로그램을 작성하라.
#
# 입력:
#   첫 번째 줄에 돌봐야 하는 시간 T (1 ≤ T ≤ 1000)
#   두 번째 줄에 가지고 있는 사탕의 총 개수 N (1 ≤ N ≤ 100)
#   세 번째 줄에 각 사탕의 맛을 나타내는 정수 F (1 ≤ F ≤ 10)들이 공백으로 구분되어 주어진다.
#
# 출력:
#   파댕이를 T분 동안 울지 않게 만들 수 있으면 "Padaeng_i Happy", 그렇지 않으면 "Padaeng_i Cry"를 출력한다.
#
# 해결 방법:
#   모든 사탕의 F값의 합이 T 이상이면 파댕이를 울지 않게 할 수 있다.
#
# 시간/공간 복잡도 : O(N)

T = int(input())
N = int(input())
F_list = list(map(int, input().split(" ")))

if T <= sum(F_list):
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")