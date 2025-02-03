# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120809
# 간단한 문제 설명 : 정수 배열 numbers가 주어질 때, numbers의 각 원소에 두배한 원소를 가진 배열을 반환하는 함수를 작성하세요.
# 해결 방법 설명 : numbers의 각 원소를 순회하며, 각 원소를 두배하여 새로운 배열에 추가하고 반환합니다.
# 시간/공간 복잡도 : 시간복잡도 O(n), 공간복잡도 O(n)

def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer