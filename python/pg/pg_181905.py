# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181905
# 간단한 문제 설명 : 문자열의 특정 구간 [s:e+1]을 뒤집어서 반환합니다.
# 해결 방법 설명 : 1. 문자열을 세 부분으로 나눕니다: 앞부분, 뒤집을 부분, 뒷부분
#                2. 가운데 부분만 뒤집어서 다시 합칩니다.
# 시간/공간 복잡도 : O(n) (문자열 길이에 비례)

def solution(my_string, s, e):
    # 문자열을 세 부분으로 분리하고 가운데 부분만 뒤집어서 합침
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]