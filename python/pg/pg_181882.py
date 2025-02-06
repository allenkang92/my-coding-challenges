# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181882
# 간단한 문제 설명 : 정수 배열 arr에서 각 원소를 조건에 맞게 변환하여 반환합니다.
#                  - 값이 50 이상인 짝수라면 해당 값을 2로 나눕니다.
#                  - 값이 50 미만인 홀수라면 해당 값을 2 곱합니다.
#                  - 아니면 원본 값을 그대로 반환합니다.
# 해결 방법 설명 : 배열의 각 원소를 순회하면서 문제에서 제시한 조건에 맞게 변환하여 결과 배열(answer)에 추가한 후 반환합니다.
# 시간/공간 복잡도 : O(n) (배열의 길이에 비례)

def solution(arr):
    answer = []
    # 배열의 각 원소에 대하여 조건에 따라 변환
    for i in arr:
        # 50 이상이며 짝수인 경우: 정수 나눗셈을 사용하여 2로 나누고 결과 배열에 추가
        if i >= 50 and i % 2 == 0:
            answer.append(i // 2)
        # 50 미만이며 홀수인 경우: 2를 곱하여 결과 배열에 추가
        elif i < 50 and i % 2 != 0:
            answer.append(i * 2)
        # 위 조건에 해당하지 않는 경우: 원본 값을 그대로 결과 배열에 추가
        else:
            answer.append(i)
    return answer