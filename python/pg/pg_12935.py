# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/12935
# 간단한 문제 설명 : 배열에서 가장 작은 수를 제거한 배열을 반환, 배열이 비어있으면 [-1] 반환
# 해결 방법 설명 : 가장 작은 수를 찾아서 제거, 배열이 1개면 [-1] 반환
# 시간/공간 복잡도 : O(n)

def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min_num = min(arr)
        arr.remove(min_num)
        return arr