# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 간단한 문제 설명 :
#   옷가게에서 구매 금액에 따른 할인율을 적용하여 최종 지불할 금액을 구하는 문제.
#
# 해결 방법 설명 :
#   - 구매 금액 price에 따라 할인율이 달라진다.
#       10만원 이상: 5% 할인
#       30만원 이상: 10% 할인
#       50만원 이상: 20% 할인
#   - 할인율은 등급이 높은 조건이 우선이다.
#   - 각 조건에 대해 price에 해당 할인율을 적용한 후, 소수점 이하는 버린다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(1) - 단순 조건문과 산술 연산만 수행
#   - 공간 복잡도: O(1) - 상수 공간만 사용

def solution(price):
    # price가 50만원 이상이면 20% 할인
    if price >= 50 * 10000:
        answer = int(price - (price * 0.2))
    # price가 30만원 이상이면 10% 할인
    elif price >= 30 * 10000:
        answer = int(price - (price * 0.1))
    # price가 10만원 이상이면 5% 할인
    elif price >= 10 * 10000:
        answer = int(price - (price * 0.05))
    # 그 외의 경우 할인 없음
    else:
        answer = price
    return answer