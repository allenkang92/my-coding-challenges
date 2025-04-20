# 문제 링크 : https://www.acmicpc.net/problem/1546
# 간단한 문제 설명 : 
#   시험 점수를 조작하는 방법
#   1. 자기 점수 중 최댓값(M)을 고름
#   2. 모든 점수를 (점수/M*100)으로 변경
#   3. 새로운 평균을 계산
#
# 해결 방법 설명 : 
#   - N개의 점수를 입력받아 리스트에 저장
#   - 최댓값(M)을 찾음
#   - 각 점수를 새로운 점수로 변환하여 저장
#   - 새로운 점수들의 평균을 계산
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - 리스트를 두 번 순회
#   - 공간 복잡도: O(N) - N개의 점수를 저장
#
# 상대오차가 10^-2 이하이면 정답이다.

N = int(input())
S = list(map(int, input().split(" ")))

M = max(S)
manipulate_score = []

for i in S:
    manipulate_score.append(i / M * 100)

print(sum(manipulate_score)/len(manipulate_score))