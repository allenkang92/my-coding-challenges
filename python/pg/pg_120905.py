# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120905
# 간단한 문제 설명 :
#   정수 n과 정수 배열 numlist가 주어질 때, numlist에서 n의 배수만 남긴 배열을 반환하는 문제입니다.
#
# 해결 방법 설명 :
#   1. numlist의 각 원소를 순회합니다.
#   2. 현재 원소가 n의 배수인지 판별하기 위해, mod 연산 (원소 % n)을 수행합니다.
#      - 만약 나머지가 0이면, 해당 원소는 n의 배수입니다.
#   3. n의 배수인 원소들을 결과 리스트에 추가합니다.
#   4. 최종 결과 리스트를 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(m) (m은 numlist의 길이)
#   - 공간 복잡도: O(m) (결과 배열에 최대 m개의 원소가 저장될 수 있음)

def solution(n, numlist):
    answer = []
    for number in numlist:
        # number가 n의 배수인지 확인. n의 배수이면 나머지가 0임.
        if number % n == 0:
            answer.append(number)
    return answer