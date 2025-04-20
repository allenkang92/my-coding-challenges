# 문제 링크 : https://www.acmicpc.net/problem/32604
# 간단한 문제 설명 : 주어진 점수 목록이 시간 순서대로 정렬되었는지 확인
# 해결 방법 설명 : 각 점수 쌍을 순회하며 이전 점수 쌍보다 두 팀의 점수가 모두 증가하지 않았는지 확인
# 시간/공간 복잡도 : O(n)

# 입력 처리
n = int(input())  # 점수 쌍의 개수 입력
scores = [tuple(map(int, input().split())) for _ in range(n)]  # 점수 쌍을 리스트로 저장

# 순서 확인
is_chronological = True
for i in range(1, n):
    prev_a, prev_b = scores[i - 1]
    curr_a, curr_b = scores[i]
    if curr_a < prev_a or curr_b < prev_b:  # 이전 점수 쌍보다 두 팀의 점수가 모두 증가하지 않았으면
        is_chronological = False
        break

# 결과 출력
print("yes" if is_chronological else "no")