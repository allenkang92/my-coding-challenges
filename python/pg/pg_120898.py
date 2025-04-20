# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120898
# 간단한 문제 설명 : 
#   머쓱이가 할머니께 축하 편지를 작성할 때,
#   글자 한 자당 2cm를 사용하여 편지지를 작성합니다.
#   주어진 축하 문구 message의 길이에 따라 필요한 편지지의 최소 가로길이(단위: cm)를 구하는 문제입니다.
#
# 해결 방법 설명 :
#   - 편지 메시지의 길이(len(message))에 2cm를 곱하여 결과를 구합니다.
#   - 공백도 문자로 취급하므로, 전체 문자 수에 2를 곱하면 됩니다.
#
# 시간/공간 복잡도 :
#   - 시간 복잡도: O(1) - 간단한 산술 연산만 수행
#   - 공간 복잡도: O(1) - 상수 공간 사용

def solution(message):
    answer = len(message) * 2
    return answer