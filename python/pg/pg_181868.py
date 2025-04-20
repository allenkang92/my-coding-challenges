# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181868
# 간단한 문제 설명 : 단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string에서 단어를 추출하여,
#                  앞에서부터 순서대로 담은 문자열 배열을 반환합니다.
# 해결 방법 설명 : 문자열 my_string에서 내장 split() 메소드를 사용하면, 공백을 기준으로 단어들을 분리하며,
#                  연속된 공백은 무시됩니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

# def solution(my_string):
#     answer = []
#     my_string = my_string.split(" ")
#     for i in my_string:
#         if i == "":
#             pass
#         else:
#             answer.append(i)
#     return answer

def solution(my_string):
    # split() 메서드 사용 시 인자를 주지 않으면 연속된 공백과 앞뒤 공백을 처리해 단어 목록을 반환함.
    answer = my_string.split()
    return answer

