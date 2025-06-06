# 문제 링크 : https://www.acmicpc.net/problem/27110
# 문제 설명:
#   설날을 맞아 부대원들을 위해 후라이드 치킨, 간장치킨, 양념치킨을 각각 N마리씩 주문하였다.
#   각 부대원은 본인이 가장 선호하는 종류의 치킨(후라이드, 간장, 양념 중 하나)을 한 마리씩 받는다.
#   부대원들의 선호도는 각각 A명(후라이드), B명(간장), C명(양념)으로 주어진다.
#   주문한 치킨 중 각 종류별로 최대 N마리만 해당 부대원에게 배부할 수 있다.
#   본인이 선호하는 종류의 치킨을 받을 수 있는 부대원 수의 최댓값을 구하는 문제입니다.
#
# 해결 방법 설명:
#   후라이드 치킨을 선호하는 부대원 중 최대 N명, 간장 치킨을 선호하는 부대원 중 최대 N명,
#   양념 치킨을 선호하는 부대원 중 최대 N명에게 원하는 치킨을 배부할 수 있다.
#   즉, 결과값은 min(N, A) + min(N, B) + min(N, C)가 된다.
#
# 시간/공간 복잡도 : O(1)

N = int(input())
A, B, C = map(int, input().split())

result = min(N, A) + min(N, B) + min(N, C)
print(result)