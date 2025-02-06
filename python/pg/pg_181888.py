# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181888
# 간단한 문제 설명 : 정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 마지막 원소까지
#                n개 간격으로 저장되어 있는 원소들을 차례로 담은 리스트를 반환합니다.
# 해결 방법 설명 : 리스트 슬라이싱(num_list[::n])을 사용하여 n개 간격으로 저장된 원소들을 추출합니다.
# 시간/공간 복잡도 : O(n) (리스트의 길이에 비례)

def solution(num_list, n):
    # 슬라이싱을 통해 첫 번째 원소부터 n개 간격으로 원소들을 추출
    answer = num_list[::n]
    return answer