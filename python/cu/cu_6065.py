# 문제 링크 : https://codeup.kr/problem.php?id=6065
# 간단한 문제 설명 : 
#   3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력하는 문제입니다.
#
# 해결 방법 설명 :
#   단순히 조건문(if)을 사용하여, 입력된 세 정수 각각이 2로 나누어떨어지는지 확인 후 짝수만 출력합니다.
#
# 시간/공간 복잡도 : O(1)

a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)