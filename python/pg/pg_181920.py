# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181920
# 간단한 문제 설명 : 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 반환합니다.
# 해결 방법 설명 : range() 함수를 사용하여 start_num부터 end_num까지 범위의 숫자를 생성한 후, 이를 리스트로 변환하여 반환합니다.
# 시간/공간 복잡도 : O(n) (리스트의 길이에 비례)

def solution(start_num, end_num):
    # range()를 사용해 start_num부터 end_num까지 생성하고 이를 리스트로 변환
    answer = list(range(start_num, end_num+1))
    return answer