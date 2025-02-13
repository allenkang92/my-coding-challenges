# 문제 링크 (주석) : https://www.acmicpc.net/problem/13277
# 간단한 문제 설명 : 두 큰 정수 A와 B를 입력받아 A*B를 출력하는 프로그램
# 해결 방법 설명 : A와 B를 정수로 변환 후 곱셈 연산 수행
# 시간/공간 복잡도 : O(1)

A, B = map(int, input().split())

print(A * B)