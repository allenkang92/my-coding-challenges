# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120892
# 문제 설명:
#   암호화된 문자열 cipher와 정수 code가 주어질 때,
#   cipher에서 code의 배수 번째 글자만을 추출하여 해독된 암호 문자열을 반환합니다.
#
# 해결 방법 설명:
#   - cipher 문자열에서 code의 배수 번째 글자는 인덱스로는 code-1, 2×code-1, … 입니다.
#   - 파이썬의 슬라이싱을 사용하여 cipher[code-1::code]로 선택합니다.
#
# 시간/공간 복잡도:
#   - 시간 복잡도: O(n) (문자열 길이에 비례)
#   - 공간 복잡도: O(n) (결과 문자열 저장)

def solution(cipher, code):
    answer = cipher[code - 1::code]
    return answer