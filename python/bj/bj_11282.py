# 문제 링크 : https://www.acmicpc.net/problem/11282
# 간단한 문제 설명 : 주어진 N에 대해 N번째 한글 글자를 출력하는 프로그램입니다.
# 해결 방법 설명 : 초성, 중성, 종성을 조합하여 글자를 생성합니다.
# 시간/공간 복잡도 : O(1)

N = int(input()) - 1  # 0 기반 인덱스로 변환

# 초성, 중성, 종성의 개수
initials_count = 19
medials_count = 21
finals_count = 28

# 초성, 중성, 종성 인덱스 계산
initial_index = N // (medials_count * finals_count)
medial_index = (N // finals_count) % medials_count
final_index = N % finals_count

# 유니코드에서 '가'의 코드 포인트
base_code = ord('가')

# 최종 글자 계산
character_code = base_code + (initial_index * medials_count * finals_count) + (medial_index * finals_count) + final_index
result_character = chr(character_code)

print(result_character)