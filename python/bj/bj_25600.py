# 문제 링크 (주석) : https://www.acmicpc.net/problem/25600
# 간단한 문제 설명 : 트라이애슬론 대회에서 참가자들의 점수를 계산하고, 가장 높은 점수를 찾는 문제
# 해결 방법 설명 : 각 참가자의 점수를 계산하고, 조건에 따라 점수를 2배로 계산한 후 최고 점수를 찾음
# 시간/공간 복잡도 : O(N) (참가자의 수에 비례하여 시간과 공간이 소요됨)

# 입력 받기

N = int(input())

score_list = []

for _ in range(N):
    a, d, g = map(int, input().split(" "))
    if a == (d+g):
        score_list.append(2 * a * (d + g))
    else:
        score_list.append(a * (d + g))

print(max(score_list))