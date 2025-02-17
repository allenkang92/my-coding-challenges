# 문제 링크 (주석) : https://www.acmicpc.net/problem/20499
# 간단한 문제 설명 :
#   K/D/A의 형식으로 주어진 다리우스의 K, D, A 스탯을 보고,
#   스탯이 "가짜(hasu)"인지 "진짜(gosu)"인지 판별하는 문제입니다.
#
# 해결 방법 설명 :            
#   만약 K+A가 D보다 작거나, D가 0이면 "hasu"를 출력하고,
#   그렇지 않으면 "gosu"를 출력합니다.
#
# 시간/공간 복잡도 : O(1)

K, D, A = map(int, input().split("/"))

if D == 0 or K + A < D:
    print("hasu")
else:
    print("gosu")