# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/340202
# 간단한 문제 설명 : 저수지의 물이 몇 달 후에 부족해지는지 계산합니다.
# 해결 방법 설명 : 1. 매달 물 사용량을 계산하고 누적합을 구합니다.
#                2. 누적 사용량이 저수지 용량을 초과하면 해당 월을 반환합니다.
#                3. 끝까지 부족하지 않으면 -1을 반환합니다.
# 시간/공간 복잡도 : O(n) (n은 change 배열의 길이)

def solution(storage, usage, change):
    total_usage = 0
    current_usage = usage  # 현재 사용량을 따로 저장
    
    for i in range(len(change)):
        current_usage = current_usage + (current_usage * change[i] // 100)  # 정수 나눗셈 사용
        total_usage += current_usage
        if total_usage > storage:
            return i
    
    return -1