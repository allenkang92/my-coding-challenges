# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 간단한 문제 설명 : 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴
# 해결 방법 설명 : 숫자를 문자열로 변환 후 리스트에 담고, reverse() 메서드로 뒤집음
# 시간/공간 복잡도 : O(n)

def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))

    return answer[::-1]