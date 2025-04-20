# 문제 링크 : https://www.acmicpc.net/problem/31518
# 간단한 문제 설명 : 세 개의 슬롯 머신 휠이 각각 숫자 7을 표시할 수 있는지 확인
# 해결 방법 설명 : 각 휠이 7을 표시할 수 있는지 확인하고, 모든 휠이 7을 표시할 수 있다면 777을, 그렇지 않으면 0을 출력
# 시간/공간 복잡도 : O(1)

# 입력 처리
n = int(input())
wheel1 = list(map(int, input().split()))
wheel2 = list(map(int, input().split()))
wheel3 = list(map(int, input().split()))

# 7 표시 가능 여부 확인
if 7 in wheel1 and 7 in wheel2 and 7 in wheel3:
    print(777)
else:
    print(0)