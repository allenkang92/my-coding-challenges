# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120825
# 간단한 문제 설명 : 
#   문자열 my_string의 각 문자를 정수 n만큼 반복하여 출력하는 문제입니다.
#
# 해결 방법 설명 : 
#   - 문자열 my_string의 각 문자를 순회하며, 해당 문자를 n번 반복한 문자열을 생성한 후, 
#     최종 결과 문자열에 누적합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(m * n) (m은 문자열 길이)
#   - 공간 복잡도: O(m * n) (반복한 문자열을 저장)

def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer