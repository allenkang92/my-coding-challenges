# 문제 링크 : https://www.acmicpc.net/problem/33651
# 간단한 문제 설명 : 
#   'UAPC' 표지판의 일부 문자가 제거된 경우, 제거된 문자들을 찾아내는 문제
#   입력 문자열은 'UAPC'에서 일부 문자를 제거하고 순서를 유지한 형태임
# 
# 해결 방법 설명 :            
#   'UAPC' 문자열의 각 글자가 입력 문자열에 존재하는지 확인
#   존재하지 않는 글자가 바로 제거된 글자임
#   제거된 글자들을 원래 순서대로 출력
# 
# 시간/공간 복잡도 : O(1) - 고정된 크기의 문자열 처리

user_input = input()

correct_word = 'UAPC'

# 'UAPC'의 각 문자가 입력 문자열에 없으면 출력
for ch in correct_word:
    if ch not in user_input:
        print(ch, end="")