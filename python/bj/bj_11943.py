# 문제 링크 : https://www.acmicpc.net/problem/11943
# 간단한 문제 설명 : 두 바구니에 있는 사과와 오렌지를 옮겨 한 바구니에는 사과만, 다른 바구니에는 오렌지만 있도록 만드는 최소 이동 횟수를 구하세요.
# 해결 방법 설명 : 두 가지 경우를 고려하여 더 작은 이동 횟수를 선택합니다.
# 시간/공간 복잡도 : O(1)

# 첫 번째 바구니의 사과와 오렌지 수 입력
A, B = map(int, input().split())

# 두 번째 바구니의 사과와 오렌지 수 입력
C, D = map(int, input().split())

# 최소 이동 횟수 계산
min_moves = min(B + C, A + D)

# 결과 출력
print(min_moves)