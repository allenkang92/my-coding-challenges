# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181915
# 간단한 문제 설명 : 문자열 my_string과 정수 배열 index_list가 주어질 때,
#                my_string에서 index_list에 있는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 반환합니다.
# 해결 방법 설명 : for문을 사용하여 index_list의 각 인덱스에 해당하는 my_string의 글자를 추출한 후,
#                이를 순서대로 연결하여 최종 문자열을 만듭니다.
# 시간/공간 복잡도 : O(n) (index_list의 길이에 비례)

def solution(my_string, index_list):
    answer = ''
    # index_list에 포함된 각 인덱스에 해당하는 문자들을 순서대로 연결합니다.
    for i in index_list:
        answer += my_string[i]
    return answer