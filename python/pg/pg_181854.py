# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181854
# 간단한 문제 설명 : 배열 arr과 정수 n이 주어질 때, arr의 길이가 홀수면 짝수 인덱스에, 
#                  짝수면 홀수 인덱스에 n을 더한 배열을 반환합니다.
# 해결 방법 설명 : arr의 길이의 홀짝 여부를 확인한 후, 각 인덱스의 홀짝 여부에 따라
#                조건에 맞게 n을 더하여 새로운 배열을 만듭니다.
# 시간/공간 복잡도 : O(n) (배열의 길이에 비례)

def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:       # 배열 길이가 짝수일 때
        for i in range(len(arr)):
            if i % 2 != 0:       # 홀수 인덱스에 n을 더함
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    else:                        # 배열 길이가 홀수일 때
        for i in range(len(arr)):
            if i % 2 == 0:       # 짝수 인덱스에 n을 더함
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    return answer