# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12916
# 간단한 문제 설명 : 문자열 내 p와 y의 개수를 비교하여 같으면 True, 다르면 False 반환
# 해결 방법 설명 : 문자열을 소문자로 변환 후 p와 y의 개수를 세어 비교
# 시간/공간 복잡도 : O(n)

def solution(s):
    s = s.lower()
    count_p = s.count("p")
    count_y = s.count("y")
    
    if count_p == count_y:
        return True
    else:
        return False