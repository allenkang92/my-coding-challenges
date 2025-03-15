# 문제 링크 (주석) : https://www.acmicpc.net/problem/13297
# 간단한 문제 설명 : 주어진 각 추정 비용의 자릿수를 계산
# 해결 방법 설명 : 각 추정 비용을 문자열로 변환하여 길이를 계산
# 시간/공간 복잡도 : O(N)

# 입력 처리
N = int(input())

# 각 추정 비용의 자릿수 계산
for _ in range(N):
    estimate = input().strip()
    print(len(estimate))