# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181874
# 간단한 문제 설명 : 문자열 myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고,
#                  "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 반환합니다.
# 해결 방법 설명 : 문자열의 각 문자를 순회하면서 "a"일 경우 "A"로, 대문자이면서 "A"가 아닐 경우 소문자로 변환하여
#                  결과 문자열에 누적합니다. 그 외의 문자는 그대로 추가합니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

def solution(myString):
    answer = ''
    # 주어진 문자열의 각 문자를 확인
    for ch in myString:
        # 만약 문자 ch가 소문자 'a'라면 'A'로 변환하여 추가
        if ch == "a":
            answer += "A"
        # 만약 문자 ch가 대문자이고 'A'가 아니라면 소문자로 변환하여 추가
        elif ch.isupper() and ch != "A":
            answer += ch.lower()
        # 그 외의 경우 원래 문자를 그대로 추가
        else:
            answer += ch
    return answer