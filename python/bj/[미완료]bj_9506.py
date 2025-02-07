# 문제 링크 (주석) : https://www.acmicpc.net/problem/9506
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

while True:
    n = int(input())
    if n == -1:
        break
    n_list = []
    for i in range(1, n):
        if n % i == 0:
            n_list.append(i)
        else :
            pass
    if sum(n_list) == n :

        print(n, " = ", " ".join(n_list).replace(" ", "+"))
    elif sum(n_list) != n:
        print(n, "is NOT Perfect.")

# 6
# 12
# 28
# -1

# 6 = 1 + 2 + 3
# 12 is NOT perfect.
# 28 = 1 + 2 + 4 + 7 + 14