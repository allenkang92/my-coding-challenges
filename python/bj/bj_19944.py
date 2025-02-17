# 문제 링크 (주석) : https://www.acmicpc.net/problem/19944
# 간단한 문제 설명 : 
#   N과 M이 주어졌을 때, M학년이 뉴비, 올드비, TLE인지 구분하는 문제입니다.
#
# 해결 방법 설명 :            
#   뉴비는 1학년과 2학년 학생이므로, M이 1이거나 2이면 "NEWBIE!"를 출력합니다.
#   올드비는 뉴비가 아니면서 M이 N 이하인 학생입니다.
#   그 외의 경우 "TLE!"를 출력합니다.
#
# 시간/공간 복잡도 : O(1)

N, M = map(int, input().split())

if M == 1 or M == 2:
    print("NEWBIE!")
elif M <= N:
    print("OLDBIE!")
else:
    print("TLE!")