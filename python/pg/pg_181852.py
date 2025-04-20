# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181852
# 간단한 문제 설명 : 정수로 이루어진 리스트 num_list에서 가장 작은 5개의 수를 제거한 후, 남은 숫자들을 반환합니다.
# 해결 방법 설명 : 5번 반복하면서 매번 리스트를 오름차순으로 정렬하고 최소값을 제거하여,
#                가장 작은 5개의 요소를 제거합니다.
# 시간/공간 복잡도 : O(5 * (n log n)) ≒ O(n log n) (정렬 비용에 의존)

def solution(num_list):
    # 가장 작은 5개의 숫자를 제거하기 위해 5번 반복
    for _ in range(5):
        # 매 반복마다 리스트를 오름차순으로 정렬
        num_list = sorted(num_list)
        # 정렬된 리스트의 첫 번째 요소(최소값)를 제거
        num_list.remove(min(num_list))
    # 남은 숫자들이 담긴 리스트 반환
    return num_list

# 간단한 문제 설명 : 정수로 이루어진 리스트 num_list에서 가장 작은 5개의 수를 제외한 나머지 수들을 오름차순으로 담은 리스트를 반환합니다.
# 해결 방법 설명 : num_list를 오름차순으로 정렬한 후, 앞에서 5개의 요소를 제거한 나머지 리스트를 반환합니다.
# 시간/공간 복잡도 : O(n log n) (정렬 비용에 의존)

# def solution(num_list):
#     # num_list를 오름차순으로 정렬
#     sorted_list = sorted(num_list)
#     # 앞의 5개 수를 제외한 나머지 수들을 반환
#     return sorted_list[5:]