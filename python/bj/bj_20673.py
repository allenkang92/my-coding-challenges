# 문제 링크 : https://www.acmicpc.net/problem/20673
# 문제 설명:
#   네버랜드 보건부는 Covid-19 위험 수준에 따라 도시들을 색상으로 구분한 차트를 발표했습니다.
#   한 도시의 지난 2주간 1백만 명당 신규 확진자 수(p)와 신규 입원자 수(q)가 주어졌을 때,
#   위험 수준에 따라 도시의 색상을 다음과 같이 정합니다.
#       - 만약 p가 50 이하이고, q가 10 이하이면 "White" (저위험)
#       - 만약 q가 30 초과이면 "Red" (고위험)
#       - 그 외의 경우는 "Yellow"
#
# 해결 방법:
#   입력으로 p와 q를 받고, 조건에 따라 도시의 색상을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

p = int(input())
q = int(input())

if q > 30:
    print("Red")
elif p <= 50 and q <= 10:
    print("White")
else:
    print("Yellow")