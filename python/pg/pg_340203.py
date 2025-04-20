# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/340203
# 간단한 문제 설명 : CPR 순서에 따라 각 행동의 단계 번호를 반환합니다.
# 해결 방법 설명 : 1. 기본 순서 리스트를 정의합니다.
#                2. 입력된 각 행동의 인덱스를 찾아 단계 번호로 변환합니다.
# 시간/공간 복잡도 : O(n) (n은 cpr 리스트의 길이)

def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    
    # 각 행동에 대해 기본 순서에서의 위치(인덱스+1)를 찾아 저장
    for action in cpr:
        answer.append(basic_order.index(action) + 1)
        
    return answer