# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181864
# 간단한 문제 설명 : 주어진 문자열 myString에서 "A"와 "B"를 서로 바꾼 문자열에 pat가 연속하는 부분 문자열로 존재하면 1, 아니면 0을 반환합니다.
# 해결 방법 설명 : 문자열의 각 문자를 순회하면서 "A"이면 "B", "B"이면 "A"로 변환한 새로운 문자열을 만들고,
#                해당 문자열에 pat이 포함되어 있는지를 검사합니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

def solution(myString, pat):
    answer = 0
    change_str = ''
    # myString의 각 문자를 검사하여 "A"는 "B"로, "B"는 "A"로 변환하여 change_str에 누적
    for ch in myString:
        if ch == "A":
            change_str += "B"
        else:
            change_str += "A"
    # 변환된 문자열에 pat이라는 부분 문자열이 존재하면 answer에 1 할당
    if pat in change_str:
        answer = 1
    else:
        answer = 0
    return answer