# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/12917
# 간단한 문제 설명 : 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬하여 새로운 문자열을 반환합니다.
# 해결 방법 설명 : sorted() 함수를 reverse 옵션과 함께 사용하고, join() 메서드로 결과를 결합합니다.
# 시간/공간 복잡도 : O(n log n)  (정렬 비용에 의해)

def solution(s):
    answer = "".join(sorted(s, reverse=True))
    return answer