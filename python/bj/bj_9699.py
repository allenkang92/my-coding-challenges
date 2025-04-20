# 문제 링크 : https://www.acmicpc.net/problem/9699
# 문제 설명:
#   쌀 자루들이 주어지면, 그 중 가장 무거운 자루(최대값)를 찾아서 Orphanage House Al-Ameen에 배정하는 문제입니다.
#
# 해결 방법 설명:
#   각 테스트 케이스마다 5개의 정수가 주어지며, 이 중 가장 큰 값을 구합니다.
#   f-string을 이용하여 "Case #x:" 형태로 출력합니다.
#
# 시간/공간 복잡도 : O(1) per 테스트 케이스

T = int(input())

for i in range(1, T + 1):
    sack_list = list(map(int, input().split()))
    print(f"Case #{i}: {max(sack_list)}")