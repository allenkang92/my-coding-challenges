# 문제 링크 (주석) : https://www.acmicpc.net/problem/16017
# 문제 설명:
#   마지막 네 자리 숫자에 대해 다음 조건을 만족하면, 해당 전화번호는 텔레마케터 번호입니다:
#     1. 첫 번째 숫자가 8 또는 9이다.
#     2. 네 번째(마지막) 숫자가 8 또는 9이다.
#     3. 두 번째와 세 번째 숫자가 같다.
#
#   텔레마케터 번호인 경우 "ignore"를 출력하고, 그렇지 않으면 "answer"를 출력합니다.
#
# 해결 방법 설명:
#   입력으로 4개의 줄에 각각 한 자리 숫자가 주어집니다.
#   각 숫자를 정수형으로 입력받은 후, 위의 조건을 만족하는지 검사합니다.
#
# 시간/공간 복잡도 : O(1)

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if (num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and (num2 == num3):
    print("ignore")
else:
    print("answer")