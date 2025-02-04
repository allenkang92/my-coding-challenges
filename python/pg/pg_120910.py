# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 간단한 문제 설명 : 
#   어떤 세균은 1시간에 두 배만큼 증식합니다.
#   처음 세균의 마리수 n과 경과한 시간 t가 주어질 때, t시간 후 세균의 수를 계산합니다.
#
# 해결 방법 설명 :
#   - 초기 세균 수를 n으로 설정합니다.
#   - t번 반복하여 매 시간마다 세균의 수를 2배로 곱합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(t) - 시간에 비례
#   - 공간 복잡도: O(1) - 상수 공간 사용

def solution(n, t):
    answer = n
    for _ in range(t):
        answer *= 2
    return answer