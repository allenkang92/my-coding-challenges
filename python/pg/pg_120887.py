# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120887
# 간단한 문제 설명 : 
#   i부터 j까지의 수들 중에서 숫자 k가 몇 번 등장하는지 세는 문제입니다.
#   예: i=1, j=13, k=1일 때, 1은 1,10,11,12,13에서 총 6번 등장
#
# 해결 방법 설명 : 
#   1. i부터 j까지의 모든 수를 문자열로 이어붙입니다.
#   2. 이어붙인 문자열에서 k의 등장 횟수를 count() 함수로 세어 반환합니다.
# 
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(n) (n은 j-i+1)
#   - 공간 복잡도: O(n log j) (숫자를 문자열로 변환하여 저장)

def solution(i, j, k):
    answer = 0
    num_line = ''
    for a in range(i, j+1):
        num_line += str(a)
    
    answer = num_line.count(str(k))
    return answer