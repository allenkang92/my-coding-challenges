# 간단한 문제 설명 : 
#   등차수열 또는 등비수열의 다음 숫자를 찾는 문제입니다.
#
# 해결 방법 설명 : 
#   1. 연속된 세 수의 차이가 일정하면 등차수열
#   2. 연속된 세 수의 비율이 일정하면 등비수열
#   3. 등차수열: 마지막 항 + 공차
#   4. 등비수열: 마지막 항 * 공비
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

def solution(common):
    answer = 0
    
    # 등차수열 확인
    if common[2] - common[1] == common[1] - common[0]:
        diff = common[1] - common[0]  # 공차
        answer = common[-1] + diff
    # 등비수열 확인
    else:
        ratio = common[1] / common[0]  # 공비
        answer = common[-1] * ratio
        
    return answer