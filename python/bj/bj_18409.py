# 문제 링크 : https://www.acmicpc.net/problem/18409
# 간단한 문제 설명 : 주어진 문자열 S에서 a, i, u, e, o의 개수를 세어 출력
# 해결 방법 설명 :
#   문자열 S의 각 문자 ch가 모음(a, i, u, e, o)인지 확인하여 카운트
# 시간/공간 복잡도 : O(N)

N = int(input())
S = input()

counting = 0
for ch in S:
    if ch in 'aiueo':
        counting += 1

print(counting)