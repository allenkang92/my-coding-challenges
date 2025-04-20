# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181860
# 간단한 문제 설명 : 빈 배열 X에 대해 flag[i]가 true이면 arr[i]를 arr[i] * 2번 추가하고,
#                  false이면 X에서 마지막 arr[i]개의 원소를 제거합니다.
# 해결 방법 설명 : flag와 arr 배열을 함께 순회하며:
#                1. flag[i]가 true면 arr[i]를 arr[i]*2번 추가
#                2. flag[i]가 false면 마지막 arr[i]개 원소 제거
# 시간/공간 복잡도 : O(n) (n은 arr의 길이)

def solution(arr, flag):
    answer = []
    for i in range(len(flag)):        # arr과 flag를 같이 순회
        if flag[i]:                   # flag[i]가 true인 경우
            answer.extend([arr[i]] * (arr[i] * 2))  # arr[i]를 arr[i]*2번 추가
        else:                         # flag[i]가 false인 경우
            answer = answer[:-arr[i]] # 마지막 arr[i]개 원소 제거
    return answer