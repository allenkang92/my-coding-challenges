# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120868
# 간단한 문제 설명 : 
# 해결 방법 설명 : 
# 시간/공간 복잡도 : 

def solution(sides):
    answer = 0
    max_side = max(sides)
    min_side = min(sides)
    
    # 기존 배열의 max값이 가장 긴 경우
    # max < min + x 를 만족하는 x의 개수
    for i in range(1, max_side + 1):
        if max_side < min_side + i:
            answer += 1
            
    # 나머지 한 변이 가장 긴 경우
    # x < side1 + side2를 만족하는 x의 개수
    for i in range(max_side + 1, (max_side + min_side)):
        if i < sides[0] + sides[1]:
            answer += 1
            
    return answer