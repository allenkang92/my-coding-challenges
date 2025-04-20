# 문제 링크 : https://www.acmicpc.net/problem/25640
# 문제 설명:
#   진호는 MBTI 심리 검사에 관심이 많아 자신의 MBTI 유형과 친구들의 MBTI 유형을 비교해보고자 합니다.
#   첫 번째 줄에 진호의 MBTI 유형이 주어지고, 두 번째 줄에는 친구의 수 N이 주어집니다.
#   이후 N개의 줄에 걸쳐 각 친구의 MBTI 유형이 주어집니다.
#   진호와 MBTI 유형이 같은 친구의 수를 구하여 출력하는 문제입니다.
#
# 해결 방법:
#   진호의 MBTI 유형과 각 친구의 MBTI 유형을 비교하여 일치하는 경우의 수를 센 후 출력합니다.
#
# 시간/공간 복잡도 : O(N)

target_mbti = input().strip()
N = int(input())
count = 0

for _ in range(N):
    friend_mbti = input().strip()
    if friend_mbti == target_mbti:
        count += 1

print(count)