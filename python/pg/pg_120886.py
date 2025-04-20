# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120886
# 간단한 문제 설명 : 
#   문자열 before와 after가 매개변수로 주어질 때, 
#   before의 문자 순서를 바꿔 after를 만들 수 있으면 1을, 
#   만들 수 없으면 0을 반환하는 문제입니다.
#
# 해결 방법 설명 : 
#   - 두 문자열을 sorted() 함수를 사용하여 정렬합니다.
#   - 정렬된 두 문자열(리스트)의 값이 같다면, before의 순서를 바꿔 after를 만들 수 있으므로 1을 반환합니다.
#   - 그렇지 않으면 0을 반환합니다.
#
# 시간/공간 복잡도 : 
#   - 시간 복잡도: O(n log n) (n은 문자열의 길이, 정렬 사용)
#   - 공간 복잡도: O(n) (정렬된 리스트 저장에 필요한 공간)

def solution(before, after):
    comp_1 = sorted(before)
    comp_2 = sorted(after)
    if comp_1 == comp_2:
        return 1
    else:
        return 0