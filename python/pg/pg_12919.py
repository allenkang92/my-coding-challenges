# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12919
# 간단한 문제 설명 : seoul 리스트에서 "Kim"의 위치를 찾아 "김서방은 x에 있다" 문자열 반환
# 해결 방법 설명 : seoul.index("Kim")을 사용하여 "Kim"의 인덱스를 찾고, f-string으로 문자열 생성
# 시간/공간 복잡도 : O(n)

def solution(seoul):
    answer = f'김서방은 {seoul.index("Kim")}에 있다'
    return answer