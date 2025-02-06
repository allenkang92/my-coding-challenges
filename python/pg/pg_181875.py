# 문제 링크 (주석) : (문제 링크 제공되지 않음)
# 간단한 문제 설명 : 문자열 배열 strArr에서 홀수번째 인덱스의 문자열은 대문자로, 짝수번째 인덱스의 문자열은 소문자로 변환하여 반환합니다.
# 해결 방법 설명 : 각 인덱스에 따라 문자열의 대소문자를 변환한 후, 결과를 리스트에 추가합니다.
# 시간/공간 복잡도 : O(n) (배열 길이에 비례)

def solution(strArr):
    answer = []
    # 배열의 각 인덱스에 대해 반복
    for idx in range(len(strArr)):
        # 짝수번째 인덱스: 모든 문자를 소문자로 변환
        if idx % 2 == 0:
            answer.append(strArr[idx].lower())
        # 홀수번째 인덱스: 모든 문자를 대문자로 변환
        else:
            answer.append(strArr[idx].upper())
    return answer