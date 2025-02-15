# 문제 링크 (주석) : https://www.acmicpc.net/problem/31610
# 간단한 문제 설명 : A원짜리 사탕을 B개, C원짜리 봉투를 1개 구매했을 때 총 비용을 계산
# 해결 방법 설명 : (A * B) + C
# 시간/공간 복잡도 : O(1)

A = int(input())
B = int(input())
C = int(input())

print((A * B) + C)