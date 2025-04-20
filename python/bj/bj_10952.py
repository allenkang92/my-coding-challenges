# 문제 링크 : https://www.acmicpc.net/problem/10952
# 간단한 문제 설명 : 
#   두 정수 A와 B를 입력받아 합을 출력
#   입력의 마지막에는 0 두 개가 들어오며, 이 때 프로그램 종료
#
# 해결 방법 설명 : 
#   - while True로 무한 반복
#   - A, B 입력 받아서 둘 다 0이면 종료
#   - 아니면 A+B 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - 입력 개수만큼 반복
#   - 공간 복잡도: O(1) - 상수 공간만 사용

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A + B)