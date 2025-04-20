# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120854
# 간단한 문제 설명 : 
#   문자열 배열 strlist의 각 원소의 길이를 담은 배열을 반환하는 문제입니다.
#
# 해결 방법 설명 :
#   - 문자열 배열 strlist의 각 요소에 대하여 len() 함수를 사용하여 길이를 구합니다.
#   - 구한 길이를 결과 배열(answer)에 추가한 후, 최종적으로 이 배열을 반환합니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(n) - strlist의 모든 원소를 한 번씩 순회
#   - 공간 복잡도: O(n) - 결과 배열에 원소의 길이를 저장(최악의 경우 모든 원소를 저장)

def solution(strlist):
    answer = []
    for word in strlist:
        answer.append(len(word))
    return answer