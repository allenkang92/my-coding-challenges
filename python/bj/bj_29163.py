# 문제 링크 (주석) : https://www.acmicpc.net/problem/29163
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

N = int(input())
line = map(int, input().split(" "))

even = 0
odd = 0
for x in line:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
if even > odd:
    print("Happy")
else:
    print("Sad")