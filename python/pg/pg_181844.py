# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181844
# 간단한 문제 설명 : 정수 배열 arr과 delete_list의 원소 중 delete_list에 포함된 원소를 모두 삭제한 후,
#                  기존 순서를 유지한 배열을 반환합니다.
# 해결 방법 설명 : arr의 각 원소를 순회하며, 해당 원소가 delete_list에 없으면 결과 리스트(answer)에 추가합니다.
# 시간/공간 복잡도 : O(n) (arr의 길이에 비례)

def solution(arr, delete_list):
    answer = []
    # arr의 각 원소를 확인하며 delete_list에 없는 값만 answer에 추가합니다.
    for i in arr:
        if i not in delete_list:
            answer.append(i)
    return answer