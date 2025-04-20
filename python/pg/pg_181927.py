# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181927
# 간단한 문제 설명 : 정수 리스트에서 마지막 원소가 그전 원소보다 크면 그 차이를 추가하고,
#                  작거나 같으면 마지막 원소의 두 배를 추가한 리스트를 반환합니다.
# 해결 방법 설명 : 리스트의 마지막 원소[-1]와 그 전 원소[-2]를 비교하여 
#                조건에 따라 새로운 값을 append()로 추가합니다.
# 시간/공간 복잡도 : O(1) (리스트 끝에 단순 추가 연산)

def solution(num_list):
    answer = []
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)
    return num_list