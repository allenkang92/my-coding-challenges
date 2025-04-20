# 문제 링크 : https://www.acmicpc.net/problem/15552
# 간단한 문제 설명 : 
#   빠른 입출력을 위해 sys.stdin.readline()을 사용하여
#   두 정수 A와 B를 입력받아 합을 출력하는 문제
#
# 해결 방법 설명 : 
#   - sys.stdin.readline()으로 입력 처리
#   - T개의 테스트케이스 반복
#   - 각 케이스마다 A+B 계산하여 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(T) - T개의 테스트케이스
#   - 공간 복잡도: O(1) - 상수 공간만 사용

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)