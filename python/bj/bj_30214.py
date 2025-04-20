# 문제 링크 : https://www.acmicpc.net/problem/30214
# 간단한 문제 설명 :
#   대회 절반 시간의 제출 수 s1과 최종 제출 수 s2가 주어진다.
#   만약 s1이 s2의 절반 이상이면 문제는 "Easy" 즉, "E"로 간주되고,
#   그렇지 않으면 문제는 "Hard" 즉, "H"로 간주된다.
#
# 해결 방법 설명 :
#   s1과 s2를 입력받고, s1 >= (s2 / 2) 조건을 만족하면 "E", 아니면 "H"를 출력한다.
#
# 시간/공간 복잡도 : O(1)

s1, s2 = map(int, input().split())

if s1 >= s2 / 2:
    print("E")
else:
    print("H")