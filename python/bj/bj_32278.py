# 문제 링크 : https://www.acmicpc.net/problem/32278
# 간단한 문제 설명 : 주어진 정수 N에 대해, 정확하게 표현할 수 있으면서 메모리를 가장 적게 차지하는 자료형(short, int, long long)을 선택
# 해결 방법 설명 : N의 값이 각 자료형의 범위 안에 있는지 확인하여 가장 작은 자료형을 선택
# 시간/공간 복잡도 : O(1)

import sys

# 입력 처리: sys.stdin.readline()을 사용하여 입력을 받고, rstrip()으로 공백 제거
N = int(sys.stdin.readline().rstrip())

# short 범위: -2^15 <= N <= 2^15 - 1
if ((-2) ** 15) <= N <= (2 ** 15 - 1):
    print('short')    
# int 범위: -2^31 <= N <= 2^31 - 1
elif ((-2) ** 31) <= N <= (2 ** 31 - 1):
    print('int')    
# long long 범위: -2^63 <= N <= 2^63 - 1
elif ((-2) ** 63) <= N <= (2 ** 63 - 1):
    print('long long')