# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120842
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(num_list, n):
    answer = []
    length = int(len(num_list) / n)
    for i in range(1, length+1):
        answer.append([])
        for j in range(n):
            for k in num_list:
                answer[j].append(k)
    return answer