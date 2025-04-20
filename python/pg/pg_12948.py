# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 간단한 문제 설명 : 핸드폰 번호의 뒷 4자리를 제외한 나머지를 *로 가립니다.
# 해결 방법 설명 : 뒷 4자리를 제외한 부분을 *로 채우고, 뒷 4자리를 이어붙입니다.
# 시간/공간 복잡도 : O(n)

def solution(phone_number):
    answer = ''
    answer += "*" * (len(phone_number) - 4)
    answer += phone_number[len(phone_number) - 4::]
    return answer