# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 간단한 문제 설명 : 
#   PROGRAMMERS-962 행성에서 나이를 알파벳으로 표현합니다.
#   a는 0, b는 1, c는 2, ..., j는 9에 해당합니다.
#
# 해결 방법 설명 : 
#   - age를 문자열로 변환한 후 각 자리 숫자별로 조건문을 사용하여 해당 알파벳으로 변환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(k) (k는 age의 자릿수)
#   - 공간 복잡도: O(k)

def solution(age):
    answer = ''
    age_to_alpha = str(age)
    for i in age_to_alpha:
        if i == '0':
            answer += 'a'
        elif i == '1':
            answer += 'b'
        elif i == '2':
            answer += 'c'
        elif i == '3':
            answer += 'd'
        elif i == '4':
            answer += 'e'
        elif i == '5':
            answer += 'f'
        elif i == '6':
            answer += 'g'
        elif i == '7':
            answer += 'h'
        elif i == '8':
            answer += 'i'
        elif i == '9':
            answer += 'j'
    return answer