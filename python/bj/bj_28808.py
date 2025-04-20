# 문제 링크 : https://www.acmicpc.net/problem/28808
# 간단한 문제 설명 : 프로그래밍 대회 참가자가 각 문제에 대해 제출한 결과를 바탕으로, 몇 개의 문제를 성공적으로 해결했는지 계산
# 해결 방법 설명 : 각 문제에 대해 첫 번째로 성공한 제출이 있는지 확인하고, 성공한 문제의 수를 계산
# 시간/공간 복잡도 : O(n * m) (n은 문제의 수, m은 각 문제당 최대 제출 횟수)

# 입력 받기
n, m = map(int, input().split())
results = [input().strip() for _ in range(n)]

# 성공한 문제 계산
solved = 0
for result in results:
    if '+' in result:
        solved += 1

# 결과 출력
print(solved)