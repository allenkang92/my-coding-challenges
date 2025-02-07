# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181862
# 간단한 문제 설명 : 문자열 myStr에서 "a", "b", "c"를 구분자로 사용해 나눠진 문자열을 반환합니다.
# 해결 방법 설명 : 문자열을 "a", "b", "c"로 대체한 후, 공백을 기준으로 split하여 나눕니다.
#                 빈 문자열은 제외하고, 결과가 빈 배열이면 ["EMPTY"]를 반환합니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

def solution(myStr):
    answer = []
    # "a", "b", "c"를 공백으로 대체
    myStr = myStr.replace("a", " ")
    myStr = myStr.replace("b", " ")
    myStr = myStr.replace("c", " ")
    # 공백을 기준으로 문자열을 나눔
    str_list = myStr.split(" ")
    # 빈 문자열을 제외하고 결과 리스트에 추가
    for ch in str_list:
        if ch != "":
            answer.append(ch)
    # 결과 리스트가 비어있으면 ["EMPTY"]를 반환
    if not answer:
        answer.append("EMPTY")
    return answer