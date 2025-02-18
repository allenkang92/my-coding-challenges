# 문제 링크 (주석) : https://www.acmicpc.net/problem/11549
# 문제 설명:
#   Blind tea tasting은 감각을 통해 차의 종류를 맞추는 문제입니다.
#   실제 차의 종류 T와 다섯 명의 참가자들이 제시한 답 A, B, C, D, E가 주어졌을 때,
#   정답 T와 일치하는 참가자의 수를 출력하는 문제입니다.
#
# 해결 방법 설명:
#   입력으로 차의 종류 T와 다섯 개의 정수를 받아 리스트의 count 함수를 사용하여 T가 몇 번 등장하는지 계산합니다.
#
# 시간/공간 복잡도 : O(1)

T = int(input())
A, B, C, D, E = map(int, input().split())

print([A, B, C, D, E].count(T))