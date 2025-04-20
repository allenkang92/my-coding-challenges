# 문제 링크 : https://www.acmicpc.net/problem/5358
# 문제 설명:
#   Football Team 문제는 키보드 오작동으로 'i'와 'e'가 서로 바뀐 이름들을
#   올바른 철자로 복원하는 문제입니다.
#
# 해결 방법 설명:
#   입력 파일의 각 줄에 대해, 모든 'i'는 'e'로, 'e'는 'i'로,
#   'I'는 'E'로, 'E'는 'I'로 변환하여 출력합니다.
#
# 시간/공간 복잡도 : O(n) (입력 문자열의 길이에 따라)
 
import sys

for name in sys.stdin:
    name = name.rstrip('\n')
    modified = ''
    for ch in name:
        if ch == "i":
            modified += "e"
        elif ch == "e":
            modified += "i"
        elif ch == "I":
            modified += "E"
        elif ch == "E":
            modified += "I"
        else:
            modified += ch
    print(modified)