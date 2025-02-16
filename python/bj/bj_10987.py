# 문제 링크 (주석) : https://www.acmicpc.net/problem/10987
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

word = input()

count = 0
for ch in word:
    if ch in ('aeiou'):
        count += 1
print(count)