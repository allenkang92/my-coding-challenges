# 문제 링크 (주석) : https://www.acmicpc.net/problem/5596
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

MK = list(map(int, input().split(" ")))
MS = list(map(int, input().split(" ")))

if sum(MK) >= sum(MS):
    print(MK)
elif sum(MS) == sum(MK):
    print(MS)