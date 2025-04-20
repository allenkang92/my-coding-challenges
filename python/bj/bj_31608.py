# 문제 링크 : https://www.acmicpc.net/problem/31608
# 간단한 문제 설명 : 두 문자열의 해밍 거리를 계산
# 해결 방법 설명 : 두 문자열을 순회하면서 같은 위치에 있는 문자가 다른 경우를 카운트
# 시간/공간 복잡도 : O(N) (N은 문자열의 길이)

# 입력 처리
N = int(input())
S = input()
T = input()

# 해밍 거리 계산
hamming_distance = 0
for i in range(N):
    if S[i] != T[i]:
        hamming_distance += 1

# 결과 출력
print(hamming_distance)