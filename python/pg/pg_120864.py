# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120864
# 간단한 문제 설명 : 
#   문자열에서 연속된 숫자들을 하나의 자연수로 보고, 모든 자연수의 합을 구합니다.
#   예: "aAb1B2cC34oOp" -> 1 + 2 + 34 = 37
#
# 해결 방법 설명 : 
#   1. 문자열에서 알파벳을 공백으로 치환하여 숫자들만 분리합니다.
#   2. 공백으로 split하여 숫자 문자열들의 리스트를 만듭니다.
#   3. 각 숫자 문자열을 정수로 변환하여 합산합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(n) (n은 문자열 길이)
#   - 공간 복잡도: O(n) (split된 문자열 저장)

def solution(my_string):
    answer = 0
    splited = []
    # 모든 알파벳을 공백으로 치환
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, " ")
            
    # 공백으로 분리하고 비어있지 않은 문자열만 정수로 변환하여 합산
    splited = my_string.split()
    for j in splited:
        if j:  # 빈 문자열이 아닌 경우만 처리
            answer += int(j)
    return answer