# 문제 링크 (주석) : https://www.acmicpc.net/problem/1264
# 문제 설명 :
#   영문 문장을 입력받아, 모음('a', 'e', 'i', 'o', 'u'의 대소문자)의 개수를 세는 문제입니다.
#
# 해결 방법 설명 :
#   각 문장을 입력받아, 각 문자에 대해 소문자로 변환한 후, 해당 문자가 'aeiou'에 속하는지 확인하여 카운트합니다.
#   입력의 끝은 '#' 한 글자인 줄로 주어집니다.
#
# 시간/공간 복잡도 : O(n) (문자열 길이에 따라)

while True:
    sentence = input()
    if sentence == '#':
        break
    count = 0
    for ch in sentence:
        if ch.lower() in 'aeiou':
            count += 1
    print(count)