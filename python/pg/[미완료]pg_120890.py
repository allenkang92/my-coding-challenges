# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120890
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(array, n):
    answer = 0
    find_n = []
    for x in array:
        find_n.append(abs(x - n))
    min_x = min(find_n)
    idx = find_n.index(min_x)
    return array[idx]