# 문제 링크: https://www.acmicpc.net/problem/16204
# 문제 설명:
#   앞면에 O와 X가 적힌 카드 N개가 있습니다.
#   이 중 M개의 카드의 앞면에는 O가 적혀 있고, 나머지 N-M개의 카드의 앞면에는 X가 적혀 있습니다.
#   카드의 뒷 면에는 O와 X를 각각 적어야 하는데, O는 K개, X는 N-K개 적을 예정입니다.
#   우리가 임의로 뒷 면에 적을 수 있도록 배정할 수 있는데, 목표는
#   앞 면과 뒷 면에 같은 문양이 적힌 카드의 최대 개수를 구하는 것입니다.
#
# 해결 방법 설명:
#   - 앞면의 O 카드에는 뒷 면으로 O를 부여하는 것이 이득입니다.
#     최대 매칭 개수는 min(앞면 O 개수, 뒷 면 O 개수) = min(M, K) 입니다.
#   - 마찬가지로, 앞면의 X 카드에는 뒷 면으로 X를 부여하는 것이 이득이며,
#     최대 매칭 개수는 min(앞면 X 개수, 뒷 면 X 개수) = min(N - M, N - K) 입니다.
#   따라서 두 값을 더한 값이 답이 됩니다.
#
# 시간/공간 복잡도: O(1)

N, M, K = map(int, input().split(" "))

result = min(M, K) + min(N - M, N - K)
print(result)