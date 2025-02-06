# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 간단한 문제 설명 : arr의 각 원소 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환합니다. 
#                나누어 떨어지는 원소가 하나도 없다면 배열에 -1을 담아 반환합니다.
# 해결 방법 설명 : 반복문을 통해 arr의 각 원소가 divisor로 나누어 떨어지는지 확인하여 answer 리스트에 추가하고, 
#                만약 빈 배열이면 [-1]을 반환하며, 최종적으로 오름차순 정렬하여 return 합니다.
# 시간/공간 복잡도 : O(n log n)  (최악의 경우 정렬 비용 때문에)

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    answer = sorted(answer)
    return answer