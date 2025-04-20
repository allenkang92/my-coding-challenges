# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 간단한 문제 설명 : 주어진 수가 하샤드 수인지 판별
# 해결 방법 설명 : 자릿수 합을 구하고, 원래 수가 자릿수 합으로 나누어 떨어지는지 확인
# 시간/공간 복잡도 : O(n)

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