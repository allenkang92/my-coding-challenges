# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181885
# 간단한 문제 설명 : 오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 완료했는지를 나타내는 boolean 배열 finished가 주어질 때,
#                  아직 완료하지 않은 할 일들을 순서대로 반환하는 함수입니다.
# 해결 방법 설명 : todo_list와 finished의 동일 인덱스 요소를 비교하여, finished가 False인 경우에만 해당 todo_list의 요소를 결과 리스트에 추가합니다.
# 시간/공간 복잡도 : O(n) (배열의 길이에 비례)

def solution(todo_list, finished):
    answer = []
    # todo_list의 각 인덱스에 대해 확인
    for i in range(len(todo_list)):
        # 현재 할 일이 완료되지 않았다면 (finished[i]가 False이면)
        if finished[i] != True:
            # 해당 할 일을 결과 리스트에 추가
            answer.append(todo_list[i])
        else:
            # 완료된 경우는 아무 작업도 하지 않음
            pass
    # 아직 완료되지 않은 할 일들의 목록을 반환
    return answer