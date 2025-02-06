# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(x):
    answer = True
    h_list = []
    for i in str(x):
        h_list.append(int(i))
    if x % sum(h_list) == 0:
        answer = True
    else :
        answer = False
    return answer