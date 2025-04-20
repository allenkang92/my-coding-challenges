# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181890
# 간단한 문제 설명 : 'l'과 'r' 중 먼저 나오는 문자를 기준으로 왼쪽 또는 오른쪽 부분을 반환합니다.
# 해결 방법 설명 : 1. str_list를 순회하며 'l'이나 'r'을 찾습니다.
#                2. 'l'이 먼저 나오면 해당 위치 왼쪽을, 'r'이 먼저 나오면 오른쪽을 반환합니다.
#                3. 둘 다 없으면 빈 리스트를 반환합니다.
# 시간/공간 복잡도 : O(n) (n은 str_list의 길이)

def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return str_list[:i]  # l의 왼쪽 부분 반환
        elif str_list[i] == 'r':
            return str_list[i+1:]  # r의 오른쪽 부분 반환
    return []  # l이나 r이 없는 경우 빈 리스트 반환