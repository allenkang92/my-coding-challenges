# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120913
# 간단한 문제 설명 : 문자열을 n길이씩 잘라서 배열로 만듭니다.
# 해결 방법 설명 : 1. 문자열을 n개씩 슬라이싱하여 리스트에 저장
#                2. range(0, len(my_str), n)으로 n간격으로 인덱스 생성
#                3. 마지막 남은 부분도 자동으로 처리됨
# 시간/공간 복잡도 : O(n) (n은 문자열의 길이)

def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):   # n간격으로 인덱스 생성
        answer.append(my_str[i: i+n])     # i부터 i+n까지 슬라이싱하여 추가
    return answer