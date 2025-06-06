# 문제 링크 : https://www.acmicpc.net/problem/15917
# 간단한 문제 설명 : 주어진 수가 2의 거듭제곱 형태(2^n)인지 판별하는 문제
# 해결 방법 설명 : 비트 연산을 활용하여 효율적으로 2의 거듭제곱 여부 판별
# 시간/공간 복잡도 : O(Q), Q는 쿼리의 개수, 각 판별은 O(1) 시간 소요

import sys
input = sys.stdin.readline  # 빠른 입력을 위한 설정

# 쿼리의 개수 입력
Q = int(input())

# 각 쿼리에 대해 처리
for _ in range(Q):
    a = int(input())
    
    # 비트 연산을 활용한 2의 거듭제곱 판별
    if (a & -a) == a:  # 2의 거듭제곱 판별
        print(1)
    else:
        print(0)