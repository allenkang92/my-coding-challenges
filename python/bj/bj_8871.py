# 문제 링크 : https://www.acmicpc.net/problem/8871
# 간단한 문제 설명 : n개의 채점 라운드와 1개의 연습 라운드로 구성된 대회에서 최소/최대 문제 수를 계산
# 해결 방법 설명 : 채점 라운드는 각 2문제 또는 3문제, 연습 라운드는 1문제이므로, 전체 문제 수를 계산
# 시간/공간 복잡도 : O(1)

n = int(input())

# 채점 라운드의 최소/최대 문제 수
min_gen = n * 2
max_gen = n * 3

# 연습 라운드 최소/최대 문제 수
min_prac = 2
max_prac = 3

# 전체 최소/최대 문제 수 계산
min_total = min_gen + min_prac
max_total = max_gen + max_prac

print(min_total, max_total)