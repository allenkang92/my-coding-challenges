# 문제 링크 (주석) : https://www.acmicpc.net/problem/1000
# 간단한 문제 설명 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 해결 방법 설명 : input 함수를 이용하여 두 정수를 입력받은 후, 두 정수를 더하여 출력하기.

# 1
A, B = input().split(",")
print(int(A) + int(B))

# 2
A, B = map(int, input().split())
print(A + B)