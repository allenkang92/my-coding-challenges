# 문제 링크 (주석) : https://www.acmicpc.net/problem/7891
# 간단한 문제 설명 : 두 정수의 합을 구하는 프로그램
# 해결 방법 설명 : 각 테스트 케이스마다 두 정수를 입력받아 합을 출력
# 시간/공간 복잡도 : O(T), T는 테스트 케이스의 수

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)