# 문제 링크 : https://www.acmicpc.net/problem/25893
# 문제 설명:
#   농구 선수의 3가지 스탯이 주어졌을 때, 각 스탯이 10 이상인 개수를 조사하여 해당하는 메시지를 출력하는 문제입니다.
#   출력은 입력된 스탯을 그대로 출력한 후, 그 다음 줄에 아래와 같이 출력합니다.
#       - 세 스탯 중 10 이상인 스탯이 없으면 "zilch"
#       - 10 이상인 스탯이 1개이면 "double"
#       - 10 이상인 스탯이 2개이면 "double-double"
#       - 10 이상인 스탯이 3개이면 "triple-double"
#   각 선수의 출력 후 빈 줄을 추가합니다.
#
# 해결 방법:
#   각 선수의 스탯을 입력받은 후, 원래 입력된 문자열을 그대로 출력하고,
#   스탯 중 10 이상인 값의 개수를 센 후 조건에 맞게 메시지를 출력합니다.
#
# 시간/공간 복잡도 : O(n)

n = int(input())
for _ in range(n):
    # 입력 라인을 그대로 저장 (스페이스 구분된 세 정수)
    line = input().rstrip()
    # 입력된 스탯들을 정수 리스트로 변환
    stats = list(map(int, line.split()))
    # 10 이상인 스탯의 개수 계산
    count = sum(1 for stat in stats if stat >= 10)
    
    # 입력된 라인 그대로 출력
    print(line)
    # 조건에 따라 메시지 출력
    if count == 0:
        print("zilch")
    elif count == 1:
        print("double")
    elif count == 2:
        print("double-double")
    elif count == 3:
        print("triple-double")
    # 각 선수 출력 후 빈 줄 추가
    print()