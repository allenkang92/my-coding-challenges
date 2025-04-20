# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120823
# 간단한 문제 설명 :
#   정수 n이 주어지면 높이와 너비가 n인 직각 이등변 삼각형을 "*"을 이용해 출력하는 문제입니다.
#
# 해결 방법 설명 :
#   - n개의 줄을 출력하며, i번째 줄에는 "*"이 i개 출력됩니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n) (n번 반복)
#   - 공간 복잡도: O(1)

n = int(input())

for i in range(1, n + 1):
    print("*" * i)