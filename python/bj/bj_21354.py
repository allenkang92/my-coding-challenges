# 문제 링크 (주석) : https://www.acmicpc.net/problem/21354
# 문제 설명:
#   Axel과 Petra가 각각 판매한 사과와 배의 개수가 주어질 때,
#   사과는 한 개에 7크로나, 배는 한 개에 13크로나에 판매됩니다.
#   두 사람이 번 돈을 계산하여, 더 많이 번 사람의 이름("Axel" 또는 "Petra")을 출력하고,
#   수익이 같으면 "lika"를 출력하는 프로그램을 작성합니다.
#
# 해결 방법:
#   입력으로 두 정수 A와 P가 주어지며,
#   Axel의 수익은 A × 7, Petra의 수익은 P × 13으로 계산합니다.
#   두 수익을 비교하여 결과에 따라 출력합니다.
#
# 시간/공간 복잡도 : O(1)

A, P = map(int, input().split(" "))

Axel_income = A * 7
Petra_income = P * 13

if Axel_income > Petra_income:
    print("Axel")
elif Axel_income < Petra_income:
    print("Petra")
else:
    print("lika")