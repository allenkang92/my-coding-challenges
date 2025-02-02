# 문제 링크 (주석) : https://www.acmicpc.net/problem/11022
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

T = int(input())

for i in range(T):
    A, B = map(int, input().split(" "))
    print(f"Case #{i + 1}: {A} + {B} = {A+B}")