# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/12922
# 간단한 문제 설명 : 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴합니다.
# 해결 방법 설명 : "수박" 문자열을 반복해 n//2번을 이어붙이고, n이 홀수인 경우 "수"를 추가합니다.
# 시간/공간 복잡도 : O(n)

def solution(n):
    answer = ''
    defaults = '수박'
    if n % 2 == 0:
        answer = defaults * (n // 2)
    else:
        answer = defaults * (n // 2) + "수"
    return answer