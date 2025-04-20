# 문제 링크 : https://www.acmicpc.net/problem/8958
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

T = int(input())

for _ in range(T):
    line = input().split("X")
    count = 0
    for o in line:
        if o == 'O':
            count += 1
    print(count)