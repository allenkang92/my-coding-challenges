# 문제 링크 : https://www.acmicpc.net/problem/27880
# 간단한 문제 설명 : 숭실대역의 깊이를 계산
# 해결 방법 설명 : 각 층 사이의 이동 방법과 이동 횟수를 바탕으로 총 깊이를 계산
# 시간/공간 복잡도 : O(n) (n은 층 사이의 이동 횟수)

# 입력 처리
total_depth = 0
for _ in range(4):
    method, steps = input().split()
    steps = int(steps)
    if method == 'Stair':
        total_depth += steps * 17
    else:
        total_depth += steps * 21

# 결과 출력
print(total_depth)