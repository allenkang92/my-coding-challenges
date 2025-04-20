# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181928
# 간단한 문제 설명 : num_list의 홀수만 이어 붙인 수와 짝수만 이어 붙인 수의 합을 반환합니다.
# 해결 방법 설명 : num_list를 순회하면서 각 숫자가 짝수인지 홀수인지 확인하여 문자열로 변환 후
#                짝수는 evens에, 홀수는 odds에 이어 붙입니다. 마지막에 두 문자열을 정수로 변환하여 더합니다.
# 시간/공간 복잡도 : O(n) (리스트의 길이에 비례)

def solution(num_list):
    answer = 0
    evens = ''  # 짝수들을 문자열로 이어 붙일 변수
    odds = ''   # 홀수들을 문자열로 이어 붙일 변수
    # 주어진 리스트의 각 숫자에 대해
    for i in num_list:
        # 0이거나 짝수이면 evens에 추가
        if i == 0 or i % 2 == 0:
            evens += str(i)
        # 홀수이면 odds에 추가
        else:
            odds += str(i)
    # 이어 붙인 문자열들을 정수로 변환하여 더한 후 반환
    answer += int(evens) + int(odds)
    return answer