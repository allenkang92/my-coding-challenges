# 문제 링크 : https://codeup.kr/problem.php?id=6064
# 간단한 문제 설명 :
#   입력된 세 정수 a, b, c 중 가장 작은 값을 3항 연산자를 중첩하여 출력하는 문제입니다.
#
# 해결 방법 설명 :
#   3항 연산자를 중첩하여 a, b, c 중 가장 작은 값을 구합니다.
#   예를 들어, a가 b와 c보다 작으면 a를, 그렇지 않으면 b와 c 중 작은 값을 선택합니다.
#
# 시간/공간 복잡도 : O(1)

a, b, c = map(int, input().split(" "))
print(a if a <= b and a <= c else (b if b <= c else c))