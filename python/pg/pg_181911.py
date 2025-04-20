# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181911
# 간단한 문제 설명 : 여러 문자열에서 지정된 부분을 추출하여 이어 붙입니다.
# 해결 방법 설명 : 1. my_strings와 parts를 같은 인덱스로 순회
#                2. 각 문자열에서 parts가 지정한 범위의 부분 문자열 추출
#                3. 추출한 부분 문자열들을 순서대로 이어 붙임
# 시간/공간 복잡도 : O(n) (n은 my_strings의 길이)

def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        s, e = parts[i]  # 시작과 끝 인덱스
        answer += my_strings[i][s:e+1]  # 부분 문자열 추출 (e+1까지 포함)
    return answer