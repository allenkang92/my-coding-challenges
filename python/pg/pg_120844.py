# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120844
# 간단한 문제 설명 : 
#   정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
#   배열 numbers의 원소를 direction 방향으로 한 칸씩 회전시킨 배열을 반환합니다.
#
# 해결 방법 설명 : 
#   - direction이 "right"인 경우:
#       마지막 원소를 추출하여 배열 앞에 추가하고 나머지 원소들을 뒤에 붙입니다.
#     예) [1,2,3] → [3] + [1,2] = [3,1,2]
#   - direction이 "left"인 경우:
#       첫 원소를 추출하여 배열의 맨 뒤에 붙이고, 나머지 원소들을 앞으로 이동합니다.
#     예) [1,2,3] → [2,3] + [1] = [2,3,1]
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n) (n은 numbers의 길이)
#   - 공간 복잡도: O(n)

def solution(numbers, direction):
    if direction == "right":
        # 오른쪽 회전: 마지막 원소를 앞으로 이동
        answer = [numbers[-1]] + numbers[:-1]
    else:
        # 왼쪽 회전: 첫 원소를 뒤로 이동
        answer = numbers[1:] + [numbers[0]]
    return answer