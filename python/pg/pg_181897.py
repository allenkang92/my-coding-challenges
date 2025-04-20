# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181897
# 간단한 문제 설명 : n값에 따라 slicer의 a,b,c를 이용해 num_list를 다르게 슬라이싱합니다.
#                  n=1: 0~b까지
#                  n=2: a~끝까지  
#                  n=3: a~b까지
#                  n=4: a~b까지 c간격으로
# 해결 방법 설명 : 파이썬의 슬라이싱 문법 [시작:끝:간격]을 사용하여 n의 각 경우에 맞게
#                num_list를 자릅니다.
# 시간/공간 복잡도 : O(k) (k는 슬라이싱으로 선택된 요소의 개수)

def solution(n, slicer, num_list):
    answer = []
    if n == 1:
        answer = num_list[:slicer[1]+1:]      # 0부터 b까지
    elif n == 2:
        answer = num_list[slicer[0]::]        # a부터 끝까지
    elif n == 3:
        answer = num_list[slicer[0]:slicer[1]+1:]  # a부터 b까지
    elif n == 4:
        answer = num_list[slicer[0]:slicer[1]+1:slicer[2]]  # a부터 b까지 c간격
    return answer