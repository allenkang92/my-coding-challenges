# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181899
# 간단한 문제 설명 : 정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 반환합니다.
# 해결 방법 설명 : range() 함수를 사용하여 start_num에서 end_num까지 -1씩 감소하는 숫자들을 반복하며 리스트에 추가합니다.
# 시간/공간 복잡도 : O(n) (반복 횟수에 비례)

def solution(start_num, end_num):
    answer = []
    # start_num에서 end_num까지 1씩 감소 (range 함수의 stop 값은 end_num-1로 설정, end_num까지 포함)
    for i in range(start_num, end_num - 1, -1):
        answer.append(i)
    return answer