# 문제 링크 : https://www.acmicpc.net/problem/30999
# 문제 설명:
#   월간 향유회에서는 민주주의적 다수결 투표 방식으로 문제의 출제 여부를 정한다.
#   N개의 문제 후보마다 M명의 출제위원이 찬반 의견을 내고,
#   과반수(출제위원의 수의 절반을 초과한 수)의 찬성을 얻은 문제가 출제된다.
#   M은 항상 홀수이다.
#
# 해결 방법 설명:
#   각 후보 문제에 대해 문자열에서 'O'의 개수를 센 후,
#   그 개수가 M//2보다 크면(과반수 이상이면) 출제되는 문제로 판단하여 카운트합니다.
#
# 시간/공간 복잡도 : O(N*M)

N, M = map(int, input().split(" "))

count = 0
for _ in range(N):
    votes = input().strip()
    if votes.count("O") > M // 2:
        count += 1

print(count)