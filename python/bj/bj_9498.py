# 문제 링크 (주석) : https://www.acmicpc.net/problem/9498
# 간단한 문제 설명 : 
#   주어진 시험 점수에 따라 등급을 A, B, C, D, F로 분류하는 프로그램을 작성한다.
#   점수 범위는 다음과 같다:
#     - 90 ~ 100점: A
#     - 80 ~ 89점: B
#     - 70 ~ 79점: C
#     - 60 ~ 69점: D
#     - 그 외: F
#
# 해결 방법 설명 : 
#   - 입력으로 받은 점수를 정수형으로 변환한다.
#   - if-elif-else 문을 사용하여 점수 범위에 따라 해당 등급을 출력한다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(1) - 상수 시간에 실행됨
#   - 공간 복잡도: O(1) - 상수 공간을 사용함

score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70: 
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")