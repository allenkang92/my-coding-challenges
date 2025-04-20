# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181870
# 간단한 문제 설명 : 문자열 배열 strArr에서 "ad"라는 부분 문자열을 포함하는 모든 문자열을 제거한 후,
#                  순서를 유지한 나머지 문자열들의 배열을 반환합니다.
# 해결 방법 설명 : strArr를 순회하면서 각 문자열에 대해 "ad"가 포함되어 있는지 확인합니다.
#                "ad"가 포함되지 않은 문자열만 결과 배열에 추가합니다.
# 시간/공간 복잡도 : O(n*m) (n: strArr의 길이, m: 각 문자열의 평균 길이)

def solution(strArr):
    answer = []
    for ch in strArr:
        if "ad" not in ch:
            answer.append(ch)
    return answer