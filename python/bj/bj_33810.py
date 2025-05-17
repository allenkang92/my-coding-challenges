# 문제 링크 : https://www.acmicpc.net/problem/33810
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 



S = input()

char = "SciComLove"

count = 0
for i in range(len(S)):
    if S[i] != char[i]:
        count += 1
    else:
        count += 0

print(count)
