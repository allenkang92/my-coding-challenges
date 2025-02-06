# 문제 링크 (주석) : https://www.acmicpc.net/problem/2941
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 
line = input()
c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
for i in c_alpha:
    if i in line:
        count += 1
    
# ljes=njak
# 6
# ddz=z=
# 3