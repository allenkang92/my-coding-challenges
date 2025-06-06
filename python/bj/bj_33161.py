# 문제 링크 : https://www.acmicpc.net/problem/33161
# 문제 설명 :
#   JOI 군이 가진 돈 A원으로, 1개당 5원인 연필을 최대 몇 개 살 수 있는지 구하는 문제입니다.
#
# 해결 방법 설명 :
#   A원을 5로 나눈 몫(A // 5)이 JOI 군이 살 수 있는 연필의 최대 개수입니다.
#
# 시간/공간 복잡도 : O(1)

A = int(input())
print(A // 5)