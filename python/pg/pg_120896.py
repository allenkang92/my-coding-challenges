# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120896
# 간단한 문제 설명 : 
#   문자열에서 한 번만 등장하는 문자를 사전 순으로 정렬하여 반환합니다.
#
# 해결 방법 설명 : 
#   1. 입력 문자열을 정렬합니다.
#   2. 각 문자에 대해 등장 횟수를 확인합니다.
#   3. 한 번만 등장하는 문자를 결과 문자열에 추가합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(n log n) (정렬로 인해)
#   - 공간 복잡도: O(n) (n은 문자열 길이)

def solution(s):
    answer = ''
    s = sorted(s)  # 문자열을 사전순으로 정렬
    for i in s:
        if s.count(i) == 1:  # 정확히 한 번만 등장하는 문자 확인
            answer += i
    return answer