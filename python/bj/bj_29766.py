# 문제 링크 : https://www.acmicpc.net/problem/29766
# 문제 설명:
#   주어진 문자열에서 "DKSH"라는 부분 문자열이 몇 번 나타나는지 구하는 문제입니다.
#
# 해결 방법 설명:
#   문자열의 count() 함수를 활용하여 "DKSH"가 등장하는 횟수를 계산합니다.
#
# 시간/공간 복잡도 : O(N) (문자열의 길이에 따라)

line = input()
print(line.count("DKSH"))