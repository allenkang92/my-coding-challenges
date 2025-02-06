# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 간단한 문제 설명 : 자연수 N의 각 자릿수 합을 구합니다.
# 해결 방법 설명 : 숫자를 문자열로 변환 후 각 자릿수를 정수로 변환하여 합산합니다.
# 시간/공간 복잡도 : O(log N) (자릿수만큼 반복)

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer