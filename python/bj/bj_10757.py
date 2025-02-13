# 문제 링크 (주석) : https://www.acmicpc.net/problem/10757
# 간단한 문제 설명 : 두 정수 A와 B를 입력받아 A+B를 출력하는 프로그램을 작성
# 해결 방법 설명 : A와 B를 문자열로 입력받아 정수로 변환 후 덧셈 연산 수행
# 시간/공간 복잡도 : O(1)

A, B = map(int, input().split())

print(A + B)