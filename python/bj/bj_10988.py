# 문제 링크 : https://www.acmicpc.net/problem/10988
# 간단한 문제 설명 : 
#   알파벳 소문자로 이루어진 단어가 팰린드롬인지 확인
#   팰린드롬은 앞뒤로 읽어도 같은 단어
#
# 해결 방법 설명 : 
#   - 단어를 입력받음
#   - 슬라이싱으로 순서대로와 역순으로 비교
#   - 같으면 1, 다르면 0 출력
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(N) - 문자열 길이만큼 비교
#   - 공간 복잡도: O(N) - 문자열 저장

word = input()

if word[::] == word[::-1]:
    print(1)
else:
    print(0)