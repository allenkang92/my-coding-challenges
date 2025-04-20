# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120826
# 간단한 문제 설명 : 
#   문자열 my_string에서 letter를 제거한 문자열을 반환합니다.
#
# 해결 방법 설명 : 
#   - 문자열의 replace() 함수를 사용하여 letter를 빈 문자열("")로 대체합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(n) - 문자열의 길이에 비례
#   - 공간 복잡도: O(n) - 결과 문자열 저장에 필요한 공간

def solution(my_string, letter):
    answer = my_string.replace(letter, "")
    return answer