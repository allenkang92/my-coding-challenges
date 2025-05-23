# 문제 링크 : https://www.acmicpc.net/problem/8370
# 간단한 문제 설명 : 비행기의 비즈니스 클래스와 이코노미 클래스의 좌석 수를 계산하는 프로그램
# 해결 방법 설명 : 비즈니스 클래스 좌석 수 (n1 * k1) + 이코노미 클래스 좌석 수 (n2 * k2)
# 시간/공간 복잡도 : O(1)

n1, k1, n2, k2 = map(int, input().split())

print((n1 * k1) +  (n2 * k2))