# 문제 링크 (주석) : https://www.acmicpc.net/problem/31656
# 간단한 문제 설명 : Bob이 키보드의 키가 눌려서 중복된 문자를 입력한 메시지를 수정
# 해결 방법 설명 : 연속된 중복 문자를 하나의 문자로 줄여서 출력
# 시간/공간 복잡도 : O(N) (N은 메시지의 길이)

# 입력 처리
S = input()

# 중복 문자 제거
result = ''
prev_char = ''
for char in S:
    if char != prev_char:
        result += char
        prev_char = char

# 결과 출력
print(result)