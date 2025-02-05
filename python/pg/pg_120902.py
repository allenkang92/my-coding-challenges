# 간단한 문제 설명 : 
#   공백으로 구분된 수식 문자열을 계산하는 문제입니다.
#   연산자는 +, -만 존재하며, 왼쪽에서 오른쪽으로 순서대로 계산합니다.
#
# 해결 방법 설명 : 
#   - 문자열을 공백으로 분리하여 리스트로 만듭니다.
#   - 첫 번째 숫자부터 시작하여 연산자와 다음 숫자를 순서대로 처리합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(n) (n은 문자열 내 토큰 개수)
#   - 공간 복잡도: O(n)

def solution(my_string):
    formula = my_string.split()
    answer = int(formula[0])
    
    for i in range(1, len(formula), 2):
        if formula[i] == '+':
            answer += int(formula[i+1])
        else:
            answer -= int(formula[i+1])
    
    return answer