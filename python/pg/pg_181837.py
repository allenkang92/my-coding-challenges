# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181837
# 간단한 문제 설명 : 팀원들이 주문한 음료 배열 order가 주어질 때, 전체 결제 금액을 계산합니다.
#                  아메리카노는 4500원, 카페라테는 5000원이며
#                  "anything"이나 음료 종류만 명시된 경우는 차가운 아메리카노로 처리합니다.
# 해결 방법 설명 : order 배열을 순회하며 각 음료가 아메리카노("americano" 또는 "anything")인 경우 4500원을,
#                그 외의 경우(카페라테)는 5000원을 더합니다.
# 시간/공간 복잡도 : O(n) (주문 목록의 길이에 비례)

def solution(order):
    answer = 0
    for ch in order:
        if "americano" in ch or "anything" in ch:
            answer += 4500
        else : 
            answer += 5000
    return answer