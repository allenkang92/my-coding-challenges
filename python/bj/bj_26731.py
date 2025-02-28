# 문제 링크 (주석) : https://www.acmicpc.net/problem/26731
# 간단한 문제 설명: 
#   영어 대문자 알파벳 26개 중 25개만 주어지는데, 빠진 한 글자를 찾는 문제
# 해결 방법 설명:
#   알파벳 대문자 A부터 Z까지의 집합에서, 입력된 25개 문자를 제외하면
#   남은 한 글자가 빠진 알파벳이 된다.
#   세트의 차집합 연산 또는 모든 알파벳을 순회하며 빠진 것을 체크하는 방식으로 해결할 수 있다.
# 시간/공간 복잡도: O(1) - 알파벳 개수는 상수이기 때문에

letter = input()

# 모든 알파벳 대문자 세트 생성 (A-Z)
all_letters = set([chr(ch) for ch in range(65, 91)])

# 입력된 문자들의 세트
input_letters = set(letter)

# 차집합으로 빠진 알파벳 찾기
missing_letter = all_letters - input_letters

# 세트에서 유일한 원소를 추출하여 출력
print(list(missing_letter)[0])