# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/12944
# 간단한 문제 설명 : 주어진 배열의 평균값을 반환합니다.
# 해결 방법 설명 : 배열의 모든 요소를 더한 후, 배열의 길이로 나눕니다.
# 시간/공간 복잡도 : O(n)

def solution(arr):
    answer = 0
    answer += sum(arr) / len(arr)
    return answer