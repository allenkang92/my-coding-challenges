# 문제 링크 (주석) : https://www.acmicpc.net/problem/2475
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

num_line = map(int, input().split(" "))

agg = []
for i in num_line:
    agg.append(i ** 2)

print(sum(agg) % 10)