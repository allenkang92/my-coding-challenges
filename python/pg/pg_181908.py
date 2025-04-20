# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181908
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181908
# 간단한 문제 설명 : 문자열 my_string에서 is_suffix가 접미사인지 확인합니다.
#                  접미사란 문자열의 뒤에서부터 연속된 부분 문자열을 의미합니다.
# 해결 방법 설명 : 문자열의 endswith() 메서드를 사용하여 is_suffix가 접미사인지 확인합니다.
#                True면 1을, False면 0을 반환합니다.
# 시간/공간 복잡도 : O(n) (n은 is_suffix의 길이)

def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))  # endswith 결과를 정수로 변환