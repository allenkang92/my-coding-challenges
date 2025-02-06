# 문제 링크 (주석) : (문제 링크 미제공)
# 간단한 문제 설명 : 알파벳 문자열 myString과 pat이 주어질 때,
#                  대소문자 구분 없이 myString 내에 pat이 연속 부분 문자열로 존재하면 1을, 그렇지 않으면 0을 반환합니다.
# 해결 방법 설명 : myString과 pat을 모두 소문자로 변환한 후, count() 메서드를 사용하여 pat의 등장 횟수를 확인합니다.
# 시간/공간 복잡도 : O(n) (문자열 길이에 비례)

def solution(myString, pat):
    answer = 0
    # 대소문자 구분 없이 비교하기 위해 모두 소문자로 변환
    myString = myString.lower()
    pat = pat.lower()
    
    # myString 내에서 pat의 등장 횟수를 카운트하여,
    # 하나 이상 발견되면 answer를 1로 설정, 그렇지 않으면 0으로 설정
    if myString.count(pat) >= 1:
        answer += 1
    else:
        answer += 0  # 이 부분은 생략 가능하지만, 조건에 맞게 명시적으로 작성함.
    
    # 결과 반환
    return answer