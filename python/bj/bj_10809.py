# 문제 링크 : https://www.acmicpc.net/problem/10809
# 간단한 문제 설명 : 
#   알파벳 소문자로만 이루어진 단어에서
#   각 알파벳의 첫 등장 위치를 찾는 프로그램
#
# 해결 방법 설명 : 
#   - string.ascii_lowercase로 알파벳 리스트 생성
#   - 각 알파벳에 대해 단어에서의 위치 찾기
#   - 결과를 리스트에 저장하고 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - N은 알파벳 개수(26)
#   - 공간 복잡도: O(1) - 고정 크기 리스트 사용

from string import ascii_lowercase

S = input()
word = []

for a in ascii_lowercase:
    if a in S:
        word.append(S.index(a))
    else:
        word.append(-1)

print(*word)