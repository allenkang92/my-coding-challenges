# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181910
# 간단한 문제 설명 : 문자열 my_string에서 뒤에서 n개의 글자만 잘라서 반환합니다.
# 해결 방법 설명 : 문자열 슬라이싱을 사용하여 뒤에서 n개의 글자를 추출합니다.
#                문자열[len(문자열)-n::]은 뒤에서 n개의 문자를 가져옵니다.
# 시간/공간 복잡도 : O(n) (n개의 문자를 추출)

def solution(my_string, n):
    answer = ''
    answer += my_string[len(my_string)-n::]  # 뒤에서 n개의 문자를 가져옴
    return answer