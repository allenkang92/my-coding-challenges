# 문제 링크 (주석) : https://www.acmicpc.net/problem/33571
# 간단한 문제 설명 : 
#   주어진 문자열에서 각 글자에 있는 구멍의 개수를 세는 문제
#   특정 알파벳과 디미고 로고(@)에는 구멍이 있음
# 
# 해결 방법 설명 :            
#   각 문자별 구멍 개수를 딕셔너리에 저장하고
#   문자열을 순회하며 총 구멍 개수를 계산
# 
# 시간/공간 복잡도 : O(n) - n은 문자열의 길이

hole_dict = {
    'A': 1, 'a': 1,
    'B': 2, 'b': 1,
    'D': 1, 'd': 1,
    'e': 1,
    'g': 1,
    'O': 1, 'o': 1,
    'P': 1, 'p': 1, 
    'Q': 1, 'q': 1,
    'R': 1,
    '@': 1
}

S = input()

hole_count = 0

for ch in S:
    if ch in hole_dict:
        hole_count += hole_dict[ch]

print(hole_count)