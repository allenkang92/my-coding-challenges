# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181894
# 간단한 문제 설명 : 배열에서 모든 2를 포함하는 가장 작은 연속 부분 배열을 찾습니다.
# 해결 방법 설명 : 1. 배열에서 2의 첫 번째와 마지막 위치를 찾습니다.
#                2. 해당 범위의 부분 배열을 반환합니다.
#                3. 2가 없으면 [-1]을 반환합니다.
# 시간/공간 복잡도 : O(n) (n은 배열의 길이)

def solution(arr):
    # 2가 없는 경우 [-1] 반환
    if 2 not in arr:
        return [-1]
    
    # 첫 번째와 마지막 2의 위치 찾기
    first = arr.index(2)
    last = len(arr) - arr[::-1].index(2) - 1
    
    # 해당 범위의 부분 배열 반환
    return arr[first:last + 1]