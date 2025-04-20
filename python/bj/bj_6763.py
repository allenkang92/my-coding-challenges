# 문제 링크 : https://www.acmicpc.net/problem/6763
# 문제 설명:
#   운전자의 속도에 따라 부과되는 벌금을 출력하는 문제입니다.
#   속도 제한보다 빨리 달리지 않은 경우 "Congratulations, you are within the speed limit!"를 출력하고,
#   과속인 경우 표에 따라 벌금을 출력합니다.
#
# 해결 방법 설명:
#   1부터 20km/h 초과이면 $100, 21부터 30km/h 초과이면 $270, 
#   31km/h 이상 초과이면 $500의 벌금을 부과합니다.
#
# 시간/공간 복잡도 : O(1)

rate_limit = int(input())
recorded = int(input())

difference = recorded - rate_limit

if difference <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 <= difference <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= difference <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")