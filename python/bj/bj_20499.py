# 문제 링크 (주석) : https://www.acmicpc.net/problem/20499
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

K, D, A = map(int, input().split("/"))

if K + A < D or D == 0:
    print("hasu")
else: 
    print("gosu")