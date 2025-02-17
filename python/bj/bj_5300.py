# 문제 링크 (주석) : https://www.acmicpc.net/problem/5300
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

N = int(input())

out_list = []
for i in range(1, N+1):
    out_list.append(i)

for s in out_list:
    if s % 6 == 0:
        out_list.insert(s, "Go!")
        
out_list.append("Go!")
print(out_list)