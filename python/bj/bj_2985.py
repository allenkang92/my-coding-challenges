# 문제 링크 : https://www.acmicpc.net/problem/2985
# 간단한 문제 설명 : 세 정수로 이루어진 등식에서 연산자와 등호가 지워진 경우, 원래 등식을 찾는 문제
# 해결 방법 설명 : 가능한 모든 경우(8가지 케이스)를 검사하여 올바른 등식을 찾음
# 시간/공간 복잡도 : O(1) - 가능한 경우의 수가 고정됨

# 세 정수 입력 받기
N, M, K = map(int, input().split())

# 가능한 모든 등식 형태 검사
if N + M == K:
    print(f"{N}+{M}={K}")
elif N - M == K:
    print(f"{N}-{M}={K}")
elif N * M == K:
    print(f"{N}*{M}={K}")
elif N / M == K:
    print(f"{N}/{M}={K}")
elif N == M + K:
    print(f"{N}={M}+{K}")
elif N == M - K:
    print(f"{N}={M}-{K}")
elif N == M * K:
    print(f"{N}={M}*{K}")
elif N == M / K:
    print(f"{N}={M}/{K}")