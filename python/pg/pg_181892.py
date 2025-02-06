# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181892
# 간단한 문제 설명 : 정수 리스트 num_list와 정수 n이 주어질 때,
#                  n번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 반환합니다.
# 해결 방법 설명 : 리스트 슬라이싱을 사용하여, 인덱스는 0부터 시작하므로 n번째 원소는 num_list[n-1]에 해당하며,
#                  n번째 원소부터 끝까지 선택하기 위해 num_list[n-1:]를 사용합니다.
# 시간/공간 복잡도 : O(n) (리스트의 길이에 비례)

def solution(num_list, n):
    answer = num_list[n-1:]
    return answer