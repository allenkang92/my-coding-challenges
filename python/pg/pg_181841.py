# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181841
# 간단한 문제 설명 : 문자열 리스트 str_list와 제외하려는 문자열 ex가 주어질 때,
#                  str_list에서 ex를 포함한 문자열을 제외하고 모든 문자열들을 순서대로 합쳐 꼬리 문자열을 만듭니다.
# 해결 방법 설명 : str_list의 각 문자열을 순회하며, ex를 포함하지 않는 문자열만 결과 문자열(answer)에 이어 붙이고 반환합니다.
# 시간/공간 복잡도 : O(n*m) (n: 리스트 길이, m: 문자열 평균 길이)

def solution(str_list, ex):
    answer = ''
    # str_list의 각 문자열을 확인합니다.
    for s in str_list:
        # 해당 문자열에 제외할 문자열 ex가 포함되어 있지 않다면
        if ex not in s:
            answer += s  # 결과 문자열에 추가합니다.
    # 완성된 꼬리 문자열을 반환합니다.
    return answer