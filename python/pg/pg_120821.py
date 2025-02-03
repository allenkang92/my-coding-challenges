# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120821
# 간단한 문제 설명 : 
#   정수가 들어 있는 배열 num_list가 매개변수로 주어지며,
#   num_list의 원소 순서를 거꾸로 뒤집은 배열을 반환하는 문제입니다.
#
# 해결 방법 설명 :
#   - 슬라이싱 연산 num_list[::-1]을 사용하여 리스트의 순서를 뒤집습니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n) - 리스트의 모든 원소를 한번씩 순회하며 뒤집음.
#   - 공간 복잡도: O(n) - 뒤집힌 리스트를 새로 생성.

def solution(num_list):
    # 슬라이싱을 이용하여 리스트 원소들의 순서를 뒤집음
    answer = num_list[::-1]
    return answer