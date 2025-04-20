# 문제 링크 : https://www.acmicpc.net/problem/9782
# 문제 설명:
#   각 줄마다 주어진 데이터 그룹의 중앙값(Median)을 구하는 문제입니다.
#   각 줄의 첫 번째 정수는 데이터의 개수 n이며, 그 후 n개의 정수가 정렬된 상태로 주어집니다.
#   n이 홀수이면 중앙값은 (n+1)/2번째 데이터이고,
#   n이 짝수이면 중앙값은 n/2번째와 (n/2)+1번째 데이터의 평균입니다.
#
# 해결 방법 설명:
#   각 줄을 입력받아, n이 0이면 종료합니다.
#   그 외에는 n에 따라 중앙값을 계산한 뒤 "Case i: " 형식으로 출력합니다.
#
# 시간/공간 복잡도 : O(n) (입력 데이터의 수에 따라)

case = 1
while True:
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        break
    n = inputs[0]
    data = inputs[1:]
    
    if n % 2 == 1:  # 홀수인 경우
        median = data[n // 2]
    else:           # 짝수인 경우
        median = (data[n // 2 - 1] + data[n // 2]) / 2
    
    print(f"Case {case}: {median:.1f}")
    case += 1