# 문제 링크 (주석) : https://www.acmicpc.net/problem/15232
# 간단한 문제 설명 : R행 C열의 직사각형을 *로 출력하는 프로그램
# 해결 방법 설명 : R번 반복하면서 각 행에 *를 C번 출력
# 시간/공간 복잡도 : O(R)

R = int(input())
C = int(input())

for _ in range(R):
    print("*" * C)