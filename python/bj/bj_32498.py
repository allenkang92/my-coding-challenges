# 문제 링크 : https://www.acmicpc.net/problem/32498
# 간단한 문제 설명 :
#   지원된 문제들의 난이도 평가 중에서, 홀수인 (2로 나누어 떨어지지 않는)
#   문제들의 개수를 세어 출력한다.
#
# 해결 방법 설명 :
#   입력받은 candidate 문제의 수 n에 대해,
#   각 문제의 난이도 d가 홀수이면 카운트를 증가시킨 후
#   최종적으로 카운트한 값을 출력한다.
#
# 시간/공간 복잡도 : O(n)

n = int(input())
excluded = 0

for _ in range(n):
    d = int(input())
    if d % 2 != 0:
        excluded += 1

print(excluded)