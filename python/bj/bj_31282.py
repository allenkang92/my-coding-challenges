# 문제 링크 : https://www.acmicpc.net/problem/31282
# 간단한 문제 설명 : 사냥개가 토끼를 따라잡기 위해 필요한 점프 횟수 계산
# 해결 방법 설명 : 사냥개와 토끼의 상대적인 속도를 고려하여 점프 횟수 계산
# 시간/공간 복잡도 : O(1)

# 입력 처리
N, M, K = map(int, input().split())

# 점프 횟수 계산
jumps = N // (K - M)
if N % (K - M) != 0:
    jumps += 1

# 결과 출력
print(jumps)