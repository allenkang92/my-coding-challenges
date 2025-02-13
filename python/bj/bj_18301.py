# 문제 링크 (주석) : https://www.acmicpc.net/problem/18301
# 간단한 문제 설명 : 주어진 n1, n2, n12 값을 이용해 Chapman 추정치(N)을 계산
# 해결 방법 설명 : 
#   N := ⌊((n1 + 1)(n2 + 1) / (n12 + 1)) - 1⌋
#   (floor 연산은 int()로 처리)
# 시간/공간 복잡도 : O(1)

N1, N2, N12 = map(int, input().split(" "))

Chapman_estimator = int(((N1 + 1) * (N2 + 1) / (N12 + 1)) - 1)
print(Chapman_estimator)