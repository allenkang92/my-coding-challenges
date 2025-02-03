# 문제 링크 (주석) : https://www.acmicpc.net/problem/1157
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

word = input()

word = word.upper()

word_count = []
for i in word:
    word_count.append(word.count(i))

if len(max(word_count)) > 1:
    print("?")
print(word_count)