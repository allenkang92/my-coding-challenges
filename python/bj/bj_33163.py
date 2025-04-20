# 문제 링크 : https://www.acmicpc.net/problem/33163
# 간단한 문제 설명 : 
#   길이 N의 문자열 S가 주어지며, 각 문자는 J, O, I 중 하나임
#   문자열의 각 문자에 대해 다음 변환을 적용:
#   - J → O
#   - O → I
#   - I → J
#   변환 후 문자열을 출력
# 
# 해결 방법 설명 :            
#   각 문자에 대해 지정된 규칙에 따라 변환 수행
#   간단한 매핑을 사용하여 구현
# 
# 시간/공간 복잡도 : O(N) - N은 문자열의 길이

# 입력 처리
N = int(input())
S = input()

# 문자 변환을 위한 매핑
char_map = {'J': 'O', 'O': 'I', 'I': 'J'}

# 변환된 문자열 생성
result = ''
for char in S:
    result += char_map[char]

# 결과 출력
print(result)