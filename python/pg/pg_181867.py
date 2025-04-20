# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181867
# 간단한 문제 설명 : 문자열을 "x"를 기준으로 나누고, 각 부분의 길이를 배열로 반환합니다.
# 해결 방법 설명 : 1. split("x")로 문자열을 "x" 기준으로 나눕니다.
#                2. 나눠진 각 부분 문자열의 길이를 계산하여 배열에 저장합니다.
# 시간/공간 복잡도 : O(n) (n은 문자열의 길이)

def solution(myString):
    answer = []
    classfication = myString.split("x")   # "x"를 기준으로 문자열을 나눔
    
    for ch in classfication:              # 각 부분 문자열의 길이를 배열에 추가
        answer.append(len(ch))
        
    return answer