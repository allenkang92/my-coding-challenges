# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120907
# 간단한 문제 설명 : 
#   수식 문자열 배열이 주어질 때, 각 수식이 옳으면 "O", 틀리면 "X"를 담은 배열을 반환합니다.
#
# 해결 방법 설명 : 
#   1. 수식 문자열을 공백을 기준으로 분리합니다.
#   2. 첫 번째 숫자, 연산자, 두 번째 숫자, 결과 숫자를 추출합니다.
#   3. 연산자에 따라 계산하고, 결과와 비교하여 "O" 또는 "X"를 answer에 추가합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(n) (n은 quiz 배열의 길이)
#   - 공간 복잡도: O(1)

def solution(quiz):
    answer = []
    for i in quiz:
        formul = i.split()
        X = int(formul[0])
        ops = formul[1]
        Y = int(formul[2])
        right_Z = int(formul[4])
        
        if ops == '-':
            Z = X - Y
        else:
            Z = X + Y
            
        if right_Z == Z:
            answer.append("O")
        else:
            answer.append("X")
    return answer