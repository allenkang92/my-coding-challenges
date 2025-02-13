# 문제 링크 (주석) : https://www.acmicpc.net/problem/15963
# 간단한 문제 설명 : 송찬이가 필요한 배터리와 선생님이 가져온 배터리가 동일한지 확인
# 해결 방법 설명 : 두 값(N, M)을 비교하여 같으면 1, 다르면 0을 출력
# 시간/공간 복잡도 : O(1)

N, M = map(int, input().split())

if N == M:
    print(1)
else:
    print(0)