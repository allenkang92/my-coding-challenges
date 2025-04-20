# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181871
# 간단한 문제 설명 : 문자열 myString에서 pat이 몇 번 등장하는지 세는 문제입니다.
# 해결 방법 설명 : 1. myString을 순회하며 각 위치에서 pat 길이만큼의 부분 문자열 확인
#                2. pat과 일치하는 경우 카운트 증가
#                3. 총 등장 횟수 반환
# 시간/공간 복잡도 : O(n*m) (n은 myString의 길이, m은 pat의 길이)

def solution(myString, pat):
    count = 0
    for i in range(len(myString) - len(pat) + 1):  # pat 길이를 고려한 범위 설정
        if myString[i:i+len(pat)] == pat:  # 현재 위치에서 pat 길이만큼의 부분 문자열 비교
            count += 1
    return count