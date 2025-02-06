# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181835
# 간단한 문제 설명 : 정수 배열 arr와 자연수 k가 주어질 때,
#                  - k가 홀수이면 arr의 모든 원소에 k를 곱하고,
#                  - k가 짝수이면 arr의 모든 원소에 k를 더한 후,
#                  변환된 arr를 반환합니다.
# 해결 방법 설명 : arr의 각 원소를 순회하며, k의 홀짝 여부에 따라 곱셈 또는 덧셈을 수행하여 결과 배열에 추가합니다.
# 시간/공간 복잡도 : O(n) (배열의 길이에 비례)

def solution(arr, k):
    answer = []
    for i in arr:
        if k % 2 != 0:  # k가 홀수인 경우
            answer.append(i * k)
        else:           # k가 짝수인 경우
            answer.append(i + k)
    return answer