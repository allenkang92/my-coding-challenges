# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181847
# 간단한 문제 설명 : 문자열로 주어진 정수 n_str에서 가장 왼쪽에 있는 연속된 0들을 제거한 문자열을 반환합니다.
# 해결 방법 설명 : 문자열을 정수로 변환했다가 다시 문자열로 변환하면 자동으로 왼쪽의 0들이 제거됩니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

def solution(n_str):
    answer = ''
    answer = str(int(n_str))  # 문자열 -> 정수 -> 문자열 변환으로 왼쪽의 0들이 제거됨
    return answer