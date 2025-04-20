# 문제 링크 : https://www.acmicpc.net/problem/2501
# 간단한 문제 설명 : 
#   N의 약수들 중 K번째로 작은 수를 출력하는 문제입니다.
#   약수가 K개보다 적으면 0을 출력합니다.
#
# 해결 방법 설명 : 
#   - 1부터 N까지 반복하면서 N의 약수를 찾습니다.
#   - 찾은 약수들을 리스트에 저장합니다.
#   - K번째 약수를 출력하거나, 약수의 개수가 부족하면 0을 출력합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) (N까지 순회)
#   - 공간 복잡도: O(N) (최악의 경우 모든 수가 약수)

N, K = map(int, input().split())

divi_list = []
for i in range(1, N+1):
    if N % i == 0:
        divi_list.append(i)

if len(divi_list) < K:
    print(0)
else:
    print(divi_list[K-1])