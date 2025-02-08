# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181834
# 간단한 문제 설명 : 알파벳 소문자로 이루어진 문자열에서 'l'보다 앞선 알파벳은 모두 'l'로 바꿉니다.
# 해결 방법 설명 : 문자열의 각 문자를 확인하여 'a'부터 'k'까지의 문자는 'l'로 변경하고,
#                나머지 문자는 그대로 둡니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

def solution(myString):
    answer = ''
    for ch in myString:
        if ch in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'):
            answer += 'l'
        else:
            answer += ch
    return answer