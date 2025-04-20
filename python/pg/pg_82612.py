# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/82612
# 간단한 문제 설명 : 놀이기구의 이용료는 첫 이용 시 price원이며, 이용할 때마다 요금이 배수로 증가합니다.
#                count번 이용할 경우 총 이용료를 계산하여 현재 가진 money와 비교, 부족한 금액을 반환합니다.
# 해결 방법 설명 : 1부터 count까지 반복하면서 fee에 price*i를 누적합니다.
#                만약 money가 fee보다 크거나 같으면 부족한 금액은 0, 그렇지 않으면 fee - money를 반환합니다.
# 시간/공간 복잡도 : O(count)

def solution(price, money, count):
    fee = 0
    answer = 0
    for i in range(1, count+1):
        fee += price * i
    if money - fee >= 0:
        answer = 0
    elif money - fee < 0:
        answer = fee - money 
    return answer