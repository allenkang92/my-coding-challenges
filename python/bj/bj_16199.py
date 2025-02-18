# 문제 링크: https://www.acmicpc.net/problem/16199
# 문제 설명:
#   한국에서는 사람의 나이를 계산하는 방식이 3가지가 있습니다.
#     1. 만 나이: 국제적으로 사용하는 방식으로, 생일이 지나야 1세가 증가합니다.
#     2. 세는 나이: 태어날 때 1세로 시작하여 매년 1월 1일에 1세가 증가합니다.
#     3. 연 나이: 현재 연도에서 태어난 해를 뺀 값입니다.
#
#   예를 들어, 생일이 2003년 3월 5일인 사람의 경우,
#     - 기준일이 2003년 4월 5일이면 만 나이는 0세, 세는 나이는 1세, 연 나이는 0세입니다.
#     - 기준일이 2004년 1월 1일이면 만 나이는 (2004-2003-1)=0세, 세는 나이는 2세, 연 나이는 1세입니다.
#
# 해결 방법 설명:
#   1. 만 나이 = 기준년도 - 출생년도, 단 기준월일이 출생월일보다 이전이면 1을 뺍니다.
#   2. 세는 나이 = 기준년도 - 출생년도 + 1
#   3. 연 나이 = 기준년도 - 출생년도
#
# 시간/공간 복잡도 : O(1)

b_year, b_month, b_day = map(int, input().split(" "))
s_year, s_month, s_day = map(int, input().split(" "))

# 만 나이 계산
international_age = s_year - b_year
if (s_month, s_day) < (b_month, b_day):
    international_age -= 1

# 세는 나이 계산
count_age = s_year - b_year + 1

# 연 나이 계산
year_age = s_year - b_year

print(international_age)
print(count_age)
print(year_age)