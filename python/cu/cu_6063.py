# 문제 링크 : https://codeup.kr/problem.php?id=6063
# 간단한 문제 설명 :
#   입력된 두 정수(a, b) 중 큰 값을 3항 연산자를 사용하여 출력하는 문제입니다.
#
# 해결 방법 설명 :
#   3항 연산자 "x if condition else y"를 사용하여, a가 b보다 크거나 같으면 a를, 그렇지 않으면 b를 선택합니다.
#
# 시간/공간 복잡도 : O(1)

a, b = map(int, input().split(" "))
print(a if a >= b else b)