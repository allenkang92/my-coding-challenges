# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181900
# 간단한 문제 설명 : 문자열 my_string에서 indices 배열에 있는 인덱스의 문자들을 제거하고 
#                  남은 문자들을 순서대로 이어 붙인 문자열을 반환합니다.
# 해결 방법 설명 : my_string의 각 인덱스를 확인하며, 해당 인덱스가 indices에 없는 경우에만
#                문자를 결과 문자열에 추가합니다.
# 시간/공간 복잡도 : O(n) (문자열의 길이에 비례)

def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i in indices:
            pass
        else:
            answer += my_string[i]
    return answer