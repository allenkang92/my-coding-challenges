# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181909
# 간단한 문제 설명 : 문자열의 모든 접미사(suffix)를 구하고 사전순으로 정렬합니다.
# 해결 방법 설명 : 1. 문자열의 각 인덱스부터 끝까지의 부분 문자열을 구합니다.
#                2. 구한 접미사들을 리스트에 저장하고 정렬합니다.
# 시간/공간 복잡도 : O(n²) (n은 문자열의 길이)
#                  - 각 접미사를 구하는데 O(n)
#                  - n개의 접미사를 정렬하는데 O(n log n)

def solution(my_string):
    answer = []
    # 각 인덱스부터 끝까지의 부분 문자열(접미사)을 구함
    for i in range(len(my_string)):
        answer.append(my_string[i::])  # 슬라이싱으로 접미사 추출
    answer = sorted(answer)  # 사전순 정렬
    return answer