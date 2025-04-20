# 문제 링크 : https://www.acmicpc.net/problem/18698
# 문제 설명:
#   Adam은 막 걷기 시작했는데, 형 Omar의 도움에도 불구하고 자주 넘어집니다.
#   Adam은 균형을 잡기 위해 걸을 때 손을 위로 들고, 손을 내리면 넘어집니다.
#   주어진 문자열에서 'U'는 손을 든 상태, 'D'는 손을 내린 상태(넘어짐)를 나타냅니다.
#   Adam이 처음으로 넘어질 때까지 몇 걸음을 걷는지를 출력하는 프로그램을 작성하세요.
#
# 해결 방법:
#   입력된 문자열을 왼쪽부터 순서대로 확인하며 'D'를 만나면 반복을 종료합니다.
#   'U'일 경우, 걸은 걸음 수를 증가시키고, 'D'가 나오기 전까지의 걸음 수를 출력합니다.
#
# 시간/공간 복잡도 : O(T), T는 테스트 케이스 수

T = int(input())
for _ in range(T):
    steps = input()
    count = 0
    for ch in steps:
        if ch == 'D':
            break
        if ch == 'U':
            count += 1
    print(count)