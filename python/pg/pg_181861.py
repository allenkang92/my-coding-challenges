# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181861
# 간단한 문제 설명 : 배열 arr의 각 원소 a에 대해, 결과 배열의 맨 뒤에 a를 a번 추가하는 작업을 반복합니다.
# 해결 방법 설명 : 이중 for문을 사용하여 arr의 각 원소(i)에 대해 i번 반복하며 answer 리스트에 i를 추가합니다.
# 시간/공간 복잡도 : O(n*m) (n: arr의 길이, m: arr의 원소들의 평균값)

def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer