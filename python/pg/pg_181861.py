# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181861
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer