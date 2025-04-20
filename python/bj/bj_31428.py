# 문제 링크 : https://www.acmicpc.net/problem/31428
# 문제 설명:
#   헬로빗이 지원하는 트랙과 같은 트랙을 지원하는 헬로빗의 친구들의 수를 구하는 문제입니다.
#
# 해결 방법 설명:
#   친구들이 지원하는 트랙에 대한 정보 리스트에서 헬로빗이 지원하는 트랙과 동일한 문자의 개수를 count() 함수를 이용해서 구합니다.
#
# 시간/공간 복잡도 : O(N)
N = int(input())
info = list(input().split(" "))
H = input()

print(info.count(H))