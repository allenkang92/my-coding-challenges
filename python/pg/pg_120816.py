# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 간단한 문제 설명 : 
#   피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때,
#   n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 구하는 문제입니다.
#
# 해결 방법 설명 :
#   - 한 판의 피자는 slice 조각이므로, n명을 만족시키기 위해서는 n을 slice로 나누고,
#     나머지가 있으면 한 판을 더 추가합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(1)
#   - 공간 복잡도: O(1)

def solution(slice, n):
    answer = n // slice
    if n % slice > 0:
        answer += 1
    return answer