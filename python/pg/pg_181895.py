# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181895
# 간단한 문제 설명 : 주어진 배열 arr에서 intervals의 두 구간에 해당하는 부분 배열을
#                  순서대로 이어 붙인 새로운 배열을 반환합니다.
# 해결 방법 설명 : 슬라이싱을 사용하여 각 구간의 배열을 추출하고,
#                첫 번째 구간 배열에 두 번째 구간 배열을 이어 붙입니다.
# 시간/공간 복잡도 : O(n) (n은 두 구간의 길이 합)

def solution(arr, intervals):
    answer = []
    answer = arr[intervals[0][0]:intervals[0][1]+1]  # 첫 번째 구간 추출
    answer += arr[intervals[1][0]:intervals[1][1]+1]  # 두 번째 구간 추출하여 이어 붙임
    
    return answer