# 문제 링크 (주석) : https://www.acmicpc.net/problem/31134
# 간단한 문제 설명 : Team LGD가 Magnus를 금지하기 시작하는 게임 번호 x에 따라, 최악의 경우에도 우승할 수 있는 최소한의 총 게임 수 n 계산
# 해결 방법 설명 : 최악의 경우를 고려하여, Team LGD가 (n + 1) / 2 게임을 이기도록 하는 최소 n 계산
# 시간/공간 복잡도 : O(T)

import sys

# 입력 처리
data = sys.stdin.readline().split()
T = int(data[0])
results = []
for i in range(1, T + 1):
    x = int(data[i])
    # 최소 n 계산: n >= 2*(x-1) + 1
    n = 2 * (x - 1) + 1
    results.append(str(n))

# 결과 출력
print('\n'.join(results))