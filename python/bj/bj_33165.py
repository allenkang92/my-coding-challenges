# 문제 링크 (주석) : https://www.acmicpc.net/problem/33165
# 간단한 문제 설명 :
#   비太郎가 T초 동안, 초당 V m의 속도로 달렸을 때,
#   총 몇 m를 달렸는지 구하는 문제.
#
# 해결 방법 설명 :
#   T와 V를 입력받고, T * V의 값을 출력하면 된다.
#
# 시간/공간 복잡도 : O(1)

T = int(input())
V = int(input())

print(T * V)