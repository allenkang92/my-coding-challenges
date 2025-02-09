# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181857
# 간단한 문제 설명 : 배열의 길이가 2의 거듭제곱이 되도록 0을 추가합니다.
# 해결 방법 설명 : 1. 현재 길이보다 큰 가장 작은 2의 거듭제곱을 찾습니다.
#                2. 그 차이만큼 0을 추가합니다.
# 시간/공간 복잡도 : O(log n) (n은 배열의 길이)

def solution(arr):
    n = 1
    while n < len(arr):    # 배열 길이보다 큰 2의 거듭제곱 찾기
        n *= 2
    
    return arr + [0] * (n - len(arr))  # 차이만큼 0 추가