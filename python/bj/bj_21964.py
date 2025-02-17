# 문제 링크 (주석) : https://www.acmicpc.net/problem/21964
# 문제 설명:
#   주어진 문자열 S의 마지막 5글자를 출력하는 문제입니다.
#
# 해결 방법 설명:
#   문자열 S의 마지막 5글자만 출력하면 됩니다.
#
# 시간/공간 복잡도 : O(1)

N = int(input())
S = input()

print(S[-5:])