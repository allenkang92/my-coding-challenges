# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181912
# 간단한 문제 설명 : 문자열 배열의 각 원소에서 s번째 위치부터 길이 l만큼의 부분 문자열을 
#                  정수로 변환하여 k보다 큰 값만 배열로 반환합니다.
# 해결 방법 설명 : 1. 각 문자열에서 s부터 s+l까지의 부분 문자열을 추출합니다.
#                2. 추출한 문자열을 정수로 변환하여 k와 비교합니다.
#                3. k보다 큰 값만 결과 배열에 추가합니다.
# 시간/공간 복잡도 : O(n) (n은 intStrs 배열의 길이)

def solution(intStrs, k, s, l):
    str_list = []
    for ch in intStrs:
        if int(ch[s:s+l]) > k:  # s위치부터 l길이만큼 잘라서 정수로 변환하여 k와 비교
            str_list.append(int(ch[s:s+l]))
            
    return str_list