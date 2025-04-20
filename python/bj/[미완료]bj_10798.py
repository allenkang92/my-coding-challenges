# 문제 링크 : https://www.acmicpc.net/problem/10798
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

line = input()
line += input()
line += input()
line += input()
line += input()

height_line = ''

for i in range(len(line)):
    height_line

height_line = line[:len(line)+1: 5]
height_line += line[1:len(line)+1: 5]
height_line += line[2:len(line)+1: 5]
height_line += line[3:len(line)+1: 5]
height_line += line[4:len(line)+1:]
print(height_line)

# ABCDE
# abcde
# 01234
# FGHIJ
# fghij

# Aa0FfBb1GgCc2HhDd3IiEe4Jj