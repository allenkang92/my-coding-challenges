# 문제 링크 : https://www.acmicpc.net/problem/2744
# 간단한 문제 설명 : 영어 소문자와 대문자로 이루어진 단어를 입력받아, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력
# 해결 방법 설명 : 문자열을 순회하며 각 문자의 대소문자를 변환
# 시간/공간 복잡도 : O(N), N은 문자열의 길이

line = input()

word = ''

for ch in line:
    if ch.islower() == True:
        word += ch.upper()
    else:
        word += ch.lower()

print(word)