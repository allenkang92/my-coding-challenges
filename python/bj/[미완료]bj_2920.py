# 문제 링크 : https://www.acmicpc.net/problem/2920
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

line = list(map(int, input().split(" ")))

for i in range(len(line)):
    if line[0] == line[1] - 1:
        print("ascending")
#     elif line[i] == line[i + 1] + 1:
#         print("descending")
#     else:
#         print("mixed")
print(line[1])