# 문제 링크: https://www.acmicpc.net/problem/17388
# 문제 설명:
#   숭고한 알고리즘 캠프의 세 대학(Soongsil, Korea, Hanyang)의 참여도가 주어진다.
#   만약 참여도의 합이 100 이상이면 "OK"를 출력하고,
#   100 미만이면 가장 참여도가 낮은 대학의 영문 이름(Soongsil, Korea, Hanyang 중 하나)의
#   첫 단어를 출력한다.
#
# 해결 방법 설명:
#   세 대학의 참여도를 입력받아 합계를 계산하고, 합계가 100 미만이면
#   최소 참여도를 가진 대학을 찾아 해당 대학의 이름을 출력한다.
#
# 시간/공간 복잡도: O(1)

s, k, h = map(int, input().split(" "))
participation = s + k + h

if participation < 100:
    if min(s, k, h) == s:
        print("Soongsil")
    elif min(s, k, h) == k:
        print("Korea")
    elif min(s, k, h) == h:
        print("Hanyang")
else:
    print("OK")