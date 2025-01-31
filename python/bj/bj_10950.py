# 문제 링크: https://www.acmicpc.net/problem/10950
# 간단한 문제 설명:
#   T개의 테스트 케이스를 입력받아 각각의 A+B를 계산하여 출력
#
# 해결 방법:
#   - T를 입력받아 정수로 변환
#   - T번 반복하면서:
#     - 각 줄에서 A와 B를 입력받아 합을 출력
#   - 각 케이스의 결과를 바로 출력
#
# 시간/공간 복잡도:
#   - 시간 복잡도: O(T)
#   - 공간 복잡도: O(1)

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)