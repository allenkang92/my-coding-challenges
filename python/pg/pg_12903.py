# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 간단한 문제 설명 : 단어 s의 가운데 글자를 반환하는 함수, 단어의 길이가 짝수라면 가운데 두 글자를 반환합니다.
# 해결 방법 설명 : 문자열 길이에 따라 홀수면 가운데 한 글자, 짝수면 가운데 두 글자를 선택합니다.
# 시간/공간 복잡도 : O(1)

def solution(s):
    answer = ''
    index = int(len(s) / 2)
    if len(s) % 2 != 0:
        answer += s[index]
    else:
        answer += s[index-1] + s[index]
    return answer