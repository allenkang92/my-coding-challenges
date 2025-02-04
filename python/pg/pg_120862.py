# 문제 설명:
#   정수 배열 numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return 합니다.
#
# 해결 방법 설명:
#   - 서로 다른 인덱스의 두 원소를 선택하여 곱한 결과들 중 최댓값을 구합니다.
#
# 시간/공간 복잡도:
#   - 시간 복잡도: O(n^2) (n은 배열의 길이)

def solution(numbers):
    max_count = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            max_count.append(numbers[i] * numbers[j])
    return max(max_count)