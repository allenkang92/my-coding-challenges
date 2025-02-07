# 문제 링크 (주석) : https://school.programmers.co.kr/learn/courses/30/lessons/181838
# 간단한 문제 설명 : 두 날짜 배열 date1, date2가 [year, month, day] 형식으로 주어질 때,
#                  date1이 date2보다 앞선 날짜면 1을, 아니면 0을 반환합니다.
# 해결 방법 설명 : 연도, 월, 일을 순서대로 비교하여 date1이 더 앞선 날짜인지 판단합니다.
#                  - 연도가 다르면 더 작은 연도가 앞선 날짜
#                  - 연도가 같으면 월을 비교
#                  - 월도 같으면 일을 비교
# 시간/공간 복잡도 : O(1)

def solution(date1, date2):
    answer = 0
    if date1[0] < date2[0]:           # 연도 비교
        answer = 1
    elif date1[0] == date2[0]:        # 연도가 같은 경우
        if date1[1] < date2[1]:       # 월 비교
            answer = 1
        elif date1[1] == date2[1]:    # 월도 같은 경우
            if date1[2] < date2[2]:   # 일 비교
                answer = 1
            elif date1[2] == date2[2]: # 일도 같은 경우
                answer = 0
            else:                      # date1의 일이 더 큰 경우
                answer = 0
        else :                        # date1의 월이 더 큰 경우
            answer = 0
    else:                            # date1의 연도가 더 큰 경우
        answer = 0
    return answer