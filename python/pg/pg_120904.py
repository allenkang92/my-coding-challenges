# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 간단한 문제 설명:
#   정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 
#   num의 그 숫자가 있는 자리 수(1부터 시작)를 return하고, 없으면 -1을 return하도록 
#   solution 함수를 완성합니다.
#
# 해결 방법 설명:
#   - num을 문자열로 변환한 뒤 각 자리를 리스트에 저장합니다.
#   - k를 문자열로 변환하여 리스트 내에 있는지 확인합니다.
#   - 있으면 해당 숫자가 처음 등장하는 인덱스에 1을 더한 값을 반환합니다.
#   - 없으면 -1을 반환합니다.
#
# 시간/공간 복잡도:
#   - 시간 복잡도: O(n) (n은 num의 자릿수)
#   - 공간 복잡도: O(n)

def solution(num, k):
    classification = list(str(num))
    if str(k) in classification:
        return classification.index(str(k)) + 1
    else:
        return -1