# 문제 링크 (주석) : https://www.acmicpc.net/problem/26566
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

from math import pi

n = int(input())
for _ in range(n):
    A1, P1 = map(int, input().split(" "))
    R1, P2 = map(int, input().split(" "))
    P1_agg = (A1 / P1)
    P2_agg = ((pi * (R1 ** 2)) / P2)
    if P1_agg >= P2_agg:
        print("Slice of pizza")
    else: 
        print("Whole pizza")
