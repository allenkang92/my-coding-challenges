# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120850
# 간단한 문제 설명 : 
#   문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 반환합니다.
#
# 해결 방법 설명 : 
#   - 문자열의 각 문자를 순회하며, 해당 문자가 숫자인지 판별합니다.
#   - 숫자인 경우 int()로 변환한 후 결과 리스트에 추가합니다.
#   - 결과 리스트를 오름차순으로 정렬하여 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n + nlogn) = O(nlogn) (n은 문자열 길이)
#   - 공간 복잡도: O(n)

def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer = sorted(answer)
    return answer