# 문제 링크 (주석) : https://www.acmicpc.net/problem/31611
# 간단한 문제 설명 : 
# 해결 방법 설명 :            
# 시간/공간 복잡도 : 

X = int(input())


day_list = ["s1", "m", "t1", "w", "t2", "f", "s2s"]


if X > len(day_list):
    day_list = day_list * (int((len(day_list) / X)) + 1)
    print(day_list.index(day_list[X-1]))
    