# 문제 링크 (주석) : https://www.acmicpc.net/problem/11283
# 간단한 문제 설명 : 주어진 한글 글자가 몇 번째 글자인지를 계산하는 프로그램입니다.
# 해결 방법 설명 : 초성, 중성, 종성을 기반으로 글자의 순서를 결정합니다.
# 시간/공간 복잡도 : O(1)

# 한글 글자 입력
char = input().strip()

# 유니코드에서 '가'의 코드 포인트
base_code = ord('가')

# 주어진 글자의 코드 포인트
char_code = ord(char)

# 초성, 중성, 종성의 개수
initials_count = 19
medials_count = 21
finals_count = 28

# 초성, 중성, 종성 인덱스 계산
index = char_code - base_code
initial_index = index // (medials_count * finals_count)
medial_index = (index // finals_count) % medials_count
final_index = index % finals_count

# 최종 글자 순서 계산
result_index = (initial_index * (medials_count * finals_count)) + (medial_index * finals_count) + final_index + 1

print(result_index)