# 문제 링크 : https://www.acmicpc.net/problem/2420
# 간단한 문제 설명 : 두 도메인의 유명도 차이를 절대값으로 출력
# 해결 방법 설명 : 두 수의 차의 절대값을 구한다.
# 시간/공간 복잡도 : O(1)

N, M = map(int, input().split())

print(abs(N-M))