# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181890
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(str_list):
    answer = []
    if ('l', 'r') not in str_list:
        answer = []
    elif 'l' in str_list and 'r' not in str_list:
        l_idx = str_list.index('l')
        answer.append(str_list[:l_idx])
    elif 'r' in str_list and 'l' not in str_list:
        r_idx = str_list.index('r')
        answer.append(str_list[r_idx:])
    elif ('l', 'r') in str_list:
        l_idx = str_list.index('l')
        r_idx = str_list.index('r')
        if l_idx < r_idx:
            answer.append(str_list[:l_idx+1])
        else:
            answer.append(str_list[r_idx:])
    return answer