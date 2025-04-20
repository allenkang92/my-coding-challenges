# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 간단한 문제 설명 : 
#   문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
#   my_string에서 인덱스 num1과 num2에 해당하는 문자를 바꾼 문자열을 반환합니다.
#
# 해결 방법 설명 : 
#   - 인덱스 num1보다 앞부분, num1과 num2 사이, num2 이후 부분을 각각 잘라서,
#     num1과 num2의 문자를 교체하여 재구성합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n) (n은 문자열 길이)
#   - 공간 복잡도: O(n)

def solution(my_string, num1, num2):
    answer = ''
    # num1 이전 부분
    answer += my_string[:num1]
    # num1 위치에 있어야 할 num2의 문자
    answer += my_string[num2]
    # num1과 num2 사이의 부분
    answer += my_string[num1+1:num2]
    # num2 위치에 있어야 할 num1의 문자
    answer += my_string[num1]
    # num2 이후의 부분
    answer += my_string[num2+1:]
    return answer