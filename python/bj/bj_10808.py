# 문제 링크 (주석) : https://www.acmicpc.net/problem/10808
# 문제 설명:
#   알파벳 소문자로만 이루어진 단어 S가 주어진다.
#   각 알파벳(a부터 z까지)이 단어에 몇 개 포함되어 있는지 구해서 공백으로 구분하여 출력하는 문제입니다.
#
# 해결 방법 설명:
#   알파벳 a부터 z까지를 key로 갖는 딕셔너리를 생성하고, 단어 S의 각 문자를 순회하며 해당 문자의 개수를 세어줍니다.
#   그 후, a부터 z까지의 순서에 따라 각 문자의 개수를 출력합니다.
#
# 시간/공간 복잡도 : O(n) (단어의 길이에 따라)
 
S = input()

# a부터 z까지 초기 개수를 0으로 설정
alpha_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

# 단어의 각 문자에 대해 개수 증가
for ch in S:
    alpha_dict[ch] += 1

# a부터 z까지 순서대로 개수를 공백으로 구분하여 출력
print(*[alpha_dict[chr(i)] for i in range(ord('a'), ord('z') + 1)])