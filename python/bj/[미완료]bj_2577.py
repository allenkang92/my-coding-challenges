# 문제 링크 (주석) : https://www.acmicpc.net/problem/2577
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

A = int(input())
B = int(input())
C = int(input())

count = {}

agg = A * B * C

agg = str(agg)

for ch in agg:
    if ch == '0':
