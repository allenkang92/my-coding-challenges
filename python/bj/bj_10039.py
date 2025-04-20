# 문제 링크 : https://www.acmicpc.net/problem/10039
# 간단한 문제 설명 : 학생들의 점수를 입력받아 40점 미만인 경우 40점으로 보정 후 평균 점수 계산
# 시간/공간 복잡도 : O(1)

scores = []
for _ in range(5):
    temp = int(input())
    if temp < 40:
        temp = 40
    scores.append(temp)

print(sum(scores) // 5)