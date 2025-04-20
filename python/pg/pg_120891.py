# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120891
# 문제 설명:
#   369게임에서 주문(order) 숫자에 3, 6, 9가 포함되어 있으면 해당 숫자당 박수를 쳐야 합니다.
#   숫자 order가 매개변수로 주어질 때, 포함된 3, 6, 9의 개수를 반환합니다.
#
# 해결 방법 설명:
#   - order를 문자열로 변환한 후, 반복문을 통해 각 자리 숫자를 확인합니다.
#   - 3, 6, 9에 해당하면 answer를 1씩 증가시킵니다.
#
# 시간/공간 복잡도:
#   - 시간 복잡도: O(n) (n은 order의 자릿수)
#   - 공간 복잡도: O(n) (문자열 변환에 필요한 공간)

def solution(order):
    answer = 0
    for digit in str(order):
        if digit in ('3', '6', '9'):
            answer += 1
    return answer