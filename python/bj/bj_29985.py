# 문제 링크 : https://www.acmicpc.net/problem/29986
# 문제 설명:
#   Carlitos는 놀이공원 모험을 즐기고 싶지만, 자신의 키 때문에 타는 놀이기구에 제한이 있다.
#   주어진 놀이기구들의 최소 키 조건과 Carlitos의 키 H가 주어질 때,
#   Carlitos가 탈 수 있는 놀이기구의 개수를 구하는 문제이다.
#
# 입력:
#   첫 번째 줄에 놀이기구의 개수 N과 Carlitos의 키 H가 주어진다. (1 ≤ N ≤ 6, 90 ≤ H ≤ 200)
#   두 번째 줄에 각 놀이기구의 최소 키 조건 A1, A2, ..., AN이 공백으로 구분되어 주어진다. (90 ≤ Ai ≤ 200)
#
# 출력:
#   Carlson이 탈 수 있는 놀이기구의 개수를 출력한다.
#
# 해결 방법:
#   각 놀이기구의 최소 키 조건과 Carlitos의 키 H를 비교하여 H가 크거나 같으면 count를 증가시킨다.
#
# 시간/공간 복잡도: O(N)

N, H = map(int, input().split())
A_list = list(map(int, input().split()))

count = 0 
for a in A_list:
    if H >= a:
        count += 1
print(count)