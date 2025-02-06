# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181866
# 간단한 문제 설명 : 문자열 myString을 "x"를 기준으로 잘라낸 후, 빈 문자열은 제외하고 사전순으로 정렬된 배열을 반환합니다.
# 해결 방법 설명 : 문자열을 split("x")로 분리한 후, 빈 문자열을 필터링하고 sorted() 함수를 사용해 사전순으로 정렬합니다.
# 시간/공간 복잡도 : O(n log n)

def solution(myString):
    myString = myString.split("x")
    space_check = []
    for space in myString:
        if space == "":
            pass
        else:
            space_check.append(space)
    answer = sorted(space_check)        
    return answer