# 문제 링크 : https://www.acmicpc.net/problem/11365
# 문제 설명:
#   암호가 뒤집힌 문자열이 주어질 때, 이를 원래 문자열로 복원하는 문제입니다.
#   입력의 마지막 줄은 "END"로 주어지며, 이는 출력하지 않습니다.
#
# 해결 방법 설명:
#   각 줄의 문자열을 뒤집어서 출력합니다.
#
# 시간/공간 복잡도 : O(n) (암호 문자열의 길이에 따라)

while True:
    line = input()
    if line == "END":
        break
    print(line[::-1])