# 문제 링크 : https://www.acmicpc.net/problem/25628
# 문제 설명:
#   햄버거 가게에서 일하는 종현이는 햄버거를 최대한 많이 만들려 합니다.
#   햄버거를 만들기 위해서는 빵 2개와 패티 1개가 필요합니다.
#   주어진 빵의 개수 A개와 패티의 개수 B개로 만들 수 있는 햄버거의 최대 개수를 구하시오.
#
# 해결 방법:
#   각 햄버거마다 빵 2개와 패티 1개가 필요하므로, 
#   만들 수 있는 햄버거의 최대 개수는 min(A // 2, B)입니다.
#
# 시간/공간 복잡도 : O(1)

A, B = map(int, input().split(" "))
print(min(A // 2, B))