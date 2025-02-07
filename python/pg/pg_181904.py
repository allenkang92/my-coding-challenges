# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181904
# 간단한 문제 설명 : 문자열 my_string과 두 정수 m, c가 주어질 때,
#                  한 줄에 m 글자씩 적었을 때, 왼쪽부터 세로로 c번째 열에 해당하는 문자를 모아 문자열로 반환합니다.
# 해결 방법 설명 : 문자열의 (c-1)번째 인덱스부터 m 간격으로 slicing하여 세로 읽은 결과를 구할 수 있습니다.
#                  다만, 작성된 코드에서는 for문을 사용해 m 간격의 모든 슬라이스를 answer 리스트에 저장하고,
#                  그 중 c번째 열 (인덱스 c-1)을 결과로 반환합니다.
# 시간/공간 복잡도 : O(n)

def solution(my_string, m, c):
    # 모든 인덱스에 대해 my_string을 m 간격으로 슬라이싱한 결과를 저장할 리스트
    answer = []
    # 문자열의 모든 인덱스(ch)에서 시작하여 m 간격으로 자른 문자열들을 계산
    for ch in range(len(my_string)):
        # my_string[ch::m]는 인덱스 ch부터 m 간격으로 문자를 선택한 부분 문자열입니다.
        answer.append(my_string[ch::m])
    # c번째 열의 문자를 반환합니다.
    # answer 리스트의 인덱스는 0부터 시작하므로 c번째 열은 answer[c-1]에 해당합니다.
    return answer[c-1]