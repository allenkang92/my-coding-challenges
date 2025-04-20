# 문제 링크 : https://www.acmicpc.net/problem/6764
# 문제 설명:
#   네 개의 깊이 측정값이 주어졌을 때,
#   측정값이 엄격하게 증가하면 "Fish Rising",
#   엄격하게 감소하면 "Fish Diving",
#   모두 같으면 "Fish At Constant Depth",
#   그 외의 경우 "No Fish"를 출력하는 문제입니다.
#
# 해결 방법 설명:
#   네 개의 입력값을 차례대로 읽어 비교 조건에 맞는 문자열을 출력합니다.
#
# 시간/공간 복잡도 : O(1)

seq1 = int(input())
seq2 = int(input())
seq3 = int(input())
seq4 = int(input())

if seq1 < seq2 < seq3 < seq4:
    print("Fish Rising")
elif seq1 > seq2 > seq3 > seq4:
    print("Fish Diving")
elif seq1 == seq2 == seq3 == seq4:
    print("Fish At Constant Depth")
else:
    print("No Fish")