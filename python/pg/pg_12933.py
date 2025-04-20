# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 간단한 문제 설명 : 정수 n의 자릿수를 내림차순으로 정렬한 새로운 정수를 반환
# 해결 방법 설명 : 정수를 문자열로 변환 후 정렬하고 다시 정수로 변환
# 시간/공간 복잡도 : O(n log n) (정렬)

def solution(n):
    answer = 0
    sorted_int = []
    for i in str(n):
        sorted_int.append(i)
    sorted_int = sorted(sorted_int, reverse=True)
    answer = int("".join(sorted_int))
    return answer