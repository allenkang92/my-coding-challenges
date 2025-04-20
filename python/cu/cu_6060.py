# 문제 링크 : https://codeup.kr/problem.php?id=6060
# 간단한 문제 설명 :
#   입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 출력하는 문제입니다.
#
# 해결 방법 설명 :
#   파이썬의 비트 단위 연산자 &를 사용하여 두 정수의 비트 and 연산을 수행합니다.
#
# 시간/공간 복잡도 : O(1)

A, B = map(int, input().split(" "))
print(A & B)