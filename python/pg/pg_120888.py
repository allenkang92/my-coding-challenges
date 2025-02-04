# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120888
# 간단한 문제 설명 : 
#   문자열 my_string에서 중복된 문자를 제거하고, 
#   각 문자가 처음 등장하는 순서대로 하나씩만 남긴 문자열을 반환합니다.
#
# 해결 방법 설명 : 
#   - my_string의 문자들을 순서대로 순회하면서, 
#     answer 문자열에 해당 문자가 없으면 추가합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n^2) (n은 문자열 길이, in 연산의 시간 복잡도 때문에)
#   - 공간 복잡도: O(n)

def solution(my_string):
    answer = ''
    check = list(my_string)
    for i in check:
        if i not in answer:
            answer += i
    return answer