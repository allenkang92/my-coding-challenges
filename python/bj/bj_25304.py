# 문제 링크 : https://www.acmicpc.net/problem/25304
# 간단한 문제 설명 : 
#   영수증의 총 금액 X와 구매한 물건의 종류 N이 주어짐
#   각 물건의 가격과 개수로 계산한 총 금액이 X와 일치하는지 확인
#
# 해결 방법 설명 : 
#   - 총 금액 X와 물건 종류 수 N을 입력받음
#   - N번 반복하면서 각 물건의 가격과 개수를 곱해 합산
#   - 합산 금액과 X를 비교하여 결과 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - N번 반복
#   - 공간 복잡도: O(1) - 상수 공간만 사용

X = int(input())
N = int(input())

total_price = 0
for _ in range(N):
    a, b = map(int, input().split())
    total_price += a * b
    
if total_price == X:
    print("Yes")
else:
    print("No")