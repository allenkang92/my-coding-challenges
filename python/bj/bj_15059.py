# 문제 링크 : https://www.acmicpc.net/problem/15059
# 문제 설명:
#   항공편에서 승객들이 원하는 식사(치킨, 소고기, 파스타)의 요청 수와 실제 제공 가능한 식사의 수가 주어진다.
#   각 종류별로 요청 수가 실제 제공 가능한 수보다 많을 경우, 그 차이만큼은 반드시 승객들이 원하는 식사를 받지 못한다.
#   세 종류의 식사에 대해 승객들이 원하는 수와 실제 제공 가능한 수의 차이(요청이 초과된 경우)의 합을 출력하는 문제입니다.
#
# 해결 방법 설명:
#   첫 번째 줄에 치킨, 소고기, 파스타의 제공 가능한 수를 나타내는 세 정수를 입력받고,
#   두 번째 줄에 치킨, 소고기, 파스타의 요청 수를 나타내는 세 정수를 입력받습니다.
#   각 종류별로 (제공 가능한 수 - 요청 수)를 계산한 후, 그 값이 음수이면 그 절대값을 누적하여,
#   최종적으로 누적된 불만족 승객 수를 출력합니다.
#
# 시간/공간 복잡도 : O(1)
 
selectable = list(map(int, input().split(" ")))
selected = list(map(int, input().split(" ")))

count = 0
for i in range(len(selectable)):
    diff = selectable[i] - selected[i]
    if diff < 0:
        count += abs(diff)
print(count)