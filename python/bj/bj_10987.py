# 문제 링크 (주석) : https://www.acmicpc.net/problem/10987
# 문제 설명:
#   알파벳 소문자로만 이루어진 단어가 주어질 때, 모음(a, e, i, o, u)의 개수를 출력하는 문제입니다.
#
# 해결 방법 설명:
#   입력받은 단어의 각 문자에 대해, 해당 문자가 모음 문자열 'aeiou'에 포함되는지 확인 후,
#   모음이면 count를 증가시키고 최종적으로 count 값을 출력합니다.
#
# 시간/공간 복잡도 : O(n) (단어의 길이를 n이라 할 때)
word = input()

count = 0
for ch in word:
    if ch in "aeiou":
        count += 1
print(count)