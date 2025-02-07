# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181838
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(date1, date2):
    answer = 0
    if date1[0] > date2[0]:
        answer = 1
    elif date1[0] == date2[0]:
        if date1[1] > date2[1]:
            answer = 0
        elif date1[1] < date2[1]:
            answer = 1
        elif date1[1] == date2[1]:
            if date1[2] == date2[2]:
                answer = 0
            elif date1[2] > date2[2]:
                answer = 0
            elif date1[2] < date2[2]:
                answer = 1
    elif date1[0] < date2[0]:
        answer = 0        
    return answer