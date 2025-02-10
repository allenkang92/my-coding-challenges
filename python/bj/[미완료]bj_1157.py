# 문제 링크 (주석) : https://www.acmicpc.net/problem/1157
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

A = input().upper().split()

list_A = list()
str_A = str(A[0])
for ch in str_A:
    list_A.append(ch)
for i in range(len(list_A)):
    if max(list_A.count()) > 1:
        print("?")
    else:
        print(max(list_A.count()))
