# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181863
# 간단한 문제 설명 : 주어진 문자열 rny_string에서 모든 문자 'm'을 "rn"으로 변경한 문자열을 반환합니다.
# 해결 방법 설명 : str의 replace() 메서드를 사용하여 'm'을 "rn"으로 치환합니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

def solution(rny_string):
    # 문자열 rny_string에서 'm'을 "rn"으로 치환한 결과를 answer에 저장
    answer = rny_string.replace("m", "rn")
    # 치환된 문자열 반환
    return answer