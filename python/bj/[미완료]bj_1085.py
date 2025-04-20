# 문제 링크 : https://www.acmicpc.net/problem/1085
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

x, y, w, h = map(int, input().split(" "))

rec_one = []
rec_two = []
rec_three = []
rec_four = []

person_position = [x, y]

for i in range(h+1):
    for j in range(w+1):
        rec_one.append((0, i))
        rec_two.append((j, h))
        rec_three.append((w, i))
        rec_four.append((j, 0))

print(rec_one)

# 6 2 10 3
# 1